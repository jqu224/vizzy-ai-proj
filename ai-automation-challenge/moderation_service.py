import json
from typing import Optional
from models import (
    ModerationDecision,
    ModerationRequest,
    ModerationResult,
    ViolationType,
)
from mock_clients import MockOpenAIClient, MockAnthropicClient


class ModerationService:
    """
    Content moderation service with a primary moderation model and
    a more nuanced secondary reviewer for borderline cases.

    Decision model:
    - allow: content is safe enough to publish
    - review: content is ambiguous and should be manually reviewed
    - block: content is a clear policy violation
    """

    def __init__(self, openai_key: str, anthropic_key: str):
        self.openai_client = MockOpenAIClient(api_key=openai_key)
        self.anthropic_client = MockAnthropicClient(api_key=anthropic_key)
        self.review_threshold = 0.35
        self.block_threshold = 0.85

    async def moderate_content(self, request: ModerationRequest) -> ModerationResult:
        """Moderate content with escalation for ambiguous cases."""
        response = await self.openai_client.moderations.create(input=request.content)
        result = response.results[0]

        scores = self._scores_to_dict(result.category_scores)
        max_category = max(scores, key=scores.get)
        max_score = scores[max_category]
        primary_violation = self._map_category_to_violation(max_category)

        provider = "openai"
        secondary_result = None
        if self._should_use_secondary_review(request.content, result.flagged, max_score):
            secondary_result = await self._run_secondary_review(
                content=request.content,
                max_category=max_category,
                max_score=max_score,
            )
            provider = "openai+anthropic"

        decision_payload = self._build_decision(
            primary_flagged=result.flagged,
            primary_violation=primary_violation,
            max_category=max_category,
            max_score=max_score,
            secondary_result=secondary_result,
        )

        return ModerationResult(
            decision=decision_payload["decision"],
            is_safe=decision_payload["is_safe"],
            requires_human_review=decision_payload["requires_human_review"],
            confidence=decision_payload["confidence"],
            violation_type=decision_payload["violation_type"],
            reasoning=decision_payload["reasoning"],
            provider=provider,
        )

    def _scores_to_dict(self, scores) -> dict:
        return {
            "hate": scores.hate,
            "violence": scores.violence,
            "sexual": scores.sexual,
            "spam": scores.spam,
        }

    def _map_category_to_violation(self, category: str) -> ViolationType:
        category_map = {
            "hate": ViolationType.HATE_SPEECH,
            "violence": ViolationType.VIOLENCE,
            "sexual": ViolationType.ADULT_CONTENT,
            "spam": ViolationType.SPAM,
        }
        return category_map.get(category, ViolationType.NONE)

    def _should_use_secondary_review(
        self, content: str, primary_flagged: bool, max_score: float
    ) -> bool:
        text = content.lower()
        contextual_terms = [
            "cook",
            "recipe",
            "kitchen",
            "food",
            "vegetable",
            "fitness",
            "gym",
            "exercise",
            "doctor",
            "medical",
            "health",
            "nurse",
        ]
        subtle_risk_terms = [
            "miracle",
            "secret",
            "doctors hate",
            "one weird trick",
            "those people",
            "you know who",
            "certain types",
        ]
        has_context = any(term in text for term in contextual_terms)
        has_subtle_risk = any(term in text for term in subtle_risk_terms)

        return (
            (primary_flagged and max_score < self.block_threshold)
            or (not primary_flagged and max_score >= self.review_threshold)
            or (primary_flagged and has_context)
            or has_subtle_risk
        )

    async def _run_secondary_review(
        self, content: str, max_category: str, max_score: float
    ) -> dict:
        review_prompt = (
            "Review this moderation decision with extra context.\n"
            f"Content: {content}\n"
            f"Primary category: {max_category}\n"
            f"Primary score: {max_score:.2f}\n"
            "Return a JSON moderation recommendation."
        )
        review_response = await self.anthropic_client.messages.create(
            model="claude-3-5-sonnet-20241022",
            messages=[{"role": "user", "content": review_prompt}],
            max_tokens=300,
        )
        return json.loads(review_response.content[0].text)

    def _build_decision(
        self,
        primary_flagged: bool,
        primary_violation: ViolationType,
        max_category: str,
        max_score: float,
        secondary_result: Optional[dict],
    ) -> dict:
        category_name = max_category.replace("_", " ")

        if secondary_result:
            secondary_violation = self._coerce_violation_type(
                secondary_result.get("violation_type", "none")
            )
            secondary_confidence = float(secondary_result.get("confidence", max_score))
            secondary_reasoning = secondary_result.get(
                "reasoning", "Secondary review was inconclusive."
            )
            secondary_requires_review = bool(
                secondary_result.get("requires_human_review", False)
            )
            secondary_is_safe = bool(secondary_result.get("is_safe", True))

            if not secondary_is_safe and not secondary_requires_review:
                return {
                    "decision": ModerationDecision.BLOCK,
                    "is_safe": False,
                    "requires_human_review": False,
                    "confidence": max(max_score, secondary_confidence),
                    "violation_type": secondary_violation,
                    "reasoning": (
                        f"Blocked after secondary review. Primary model saw {category_name} "
                        f"at {max_score:.2f}; secondary reviewer confirmed: {secondary_reasoning}"
                    ),
                }

            if secondary_requires_review:
                return {
                    "decision": ModerationDecision.REVIEW,
                    "is_safe": False,
                    "requires_human_review": True,
                    "confidence": max(max_score, secondary_confidence),
                    "violation_type": (
                        secondary_violation
                        if secondary_violation != ViolationType.NONE
                        else primary_violation
                    ),
                    "reasoning": (
                        f"Escalated to human review. Primary model saw {category_name} "
                        f"at {max_score:.2f}; secondary reviewer said: {secondary_reasoning}"
                    ),
                }

            if primary_flagged and secondary_is_safe:
                return {
                    "decision": ModerationDecision.ALLOW,
                    "is_safe": True,
                    "requires_human_review": False,
                    "confidence": secondary_confidence,
                    "violation_type": ViolationType.NONE,
                    "reasoning": (
                        f"Allowed after secondary review. Primary model flagged {category_name} "
                        f"at {max_score:.2f}, but secondary reviewer found contextual evidence: "
                        f"{secondary_reasoning}"
                    ),
                }

            if not primary_flagged and not secondary_is_safe:
                return {
                    "decision": ModerationDecision.REVIEW,
                    "is_safe": False,
                    "requires_human_review": True,
                    "confidence": max(max_score, secondary_confidence),
                    "violation_type": secondary_violation,
                    "reasoning": (
                        f"Escalated after secondary review found additional risk: "
                        f"{secondary_reasoning}"
                    ),
                }

        if primary_flagged and max_score >= self.block_threshold:
            return {
                "decision": ModerationDecision.BLOCK,
                "is_safe": False,
                "requires_human_review": False,
                "confidence": max_score,
                "violation_type": primary_violation,
                "reasoning": (
                    f"Blocked by primary moderation for {category_name} "
                    f"with high confidence ({max_score:.2f})."
                ),
            }

        if primary_flagged:
            return {
                "decision": ModerationDecision.REVIEW,
                "is_safe": False,
                "requires_human_review": True,
                "confidence": max_score,
                "violation_type": primary_violation,
                "reasoning": (
                    f"Primary moderation flagged {category_name} at {max_score:.2f}, "
                    "but confidence is not high enough for an automatic block."
                ),
            }

        if max_score >= self.review_threshold:
            return {
                "decision": ModerationDecision.REVIEW,
                "is_safe": False,
                "requires_human_review": True,
                "confidence": max_score,
                "violation_type": primary_violation,
                "reasoning": (
                    f"Primary moderation detected borderline {category_name} risk "
                    f"at {max_score:.2f}."
                ),
            }

        return {
            "decision": ModerationDecision.ALLOW,
            "is_safe": True,
            "requires_human_review": False,
            "confidence": max_score,
            "violation_type": ViolationType.NONE,
            "reasoning": (
                f"Allowed by primary moderation. Highest risk category was {category_name} "
                f"with low confidence ({max_score:.2f})."
            ),
        }

    def _coerce_violation_type(self, violation_type: str) -> ViolationType:
        try:
            return ViolationType(violation_type)
        except ValueError:
            return ViolationType.NONE
