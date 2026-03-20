import pytest

from models import ModerationDecision, ModerationRequest, ViolationType
from moderation_service import ModerationService


@pytest.fixture
def service() -> ModerationService:
    return ModerationService(openai_key="mock-key", anthropic_key="mock-key")


async def moderate(service: ModerationService, content: str):
    request = ModerationRequest(content=content, creator_id="creator-123", video_id="video-123")
    return await service.moderate_content(request)


@pytest.mark.asyncio
async def test_cooking_content_is_allowed_after_contextual_review(service: ModerationService):
    result = await moderate(
        service,
        "Watch my kitchen recipe where I chop vegetables with a chef knife.",
    )

    assert result.decision == ModerationDecision.ALLOW
    assert result.is_safe is True
    assert result.requires_human_review is False
    assert result.violation_type == ViolationType.NONE
    assert result.provider == "openai+anthropic"
    assert "Allowed after secondary review" in result.reasoning


@pytest.mark.asyncio
async def test_fitness_content_is_allowed_after_contextual_review(service: ModerationService):
    result = await moderate(
        service,
        "My gym workout is shirtless but focused on fitness training and exercise.",
    )

    assert result.decision == ModerationDecision.ALLOW
    assert result.is_safe is True
    assert result.violation_type == ViolationType.NONE
    assert result.provider == "openai+anthropic"


@pytest.mark.asyncio
async def test_medical_content_is_sent_to_human_review(service: ModerationService):
    result = await moderate(
        service,
        "This medical training explains surgery, blood, and wound care for nurses.",
    )

    assert result.decision == ModerationDecision.REVIEW
    assert result.is_safe is False
    assert result.requires_human_review is True
    assert result.violation_type == ViolationType.VIOLENCE
    assert "human review" in result.reasoning.lower()


@pytest.mark.asyncio
async def test_supplement_scam_is_escalated_for_review(service: ModerationService):
    result = await moderate(
        service,
        "Doctors hate this one weird trick for weight loss supplements and energy.",
    )

    assert result.decision == ModerationDecision.REVIEW
    assert result.is_safe is False
    assert result.requires_human_review is True
    assert result.violation_type == ViolationType.SPAM
    assert result.provider == "openai+anthropic"


@pytest.mark.asyncio
async def test_coded_hate_speech_is_escalated_for_review(service: ModerationService):
    result = await moderate(
        service,
        "You know who should not be welcome here because certain types ruin everything.",
    )

    assert result.decision == ModerationDecision.REVIEW
    assert result.is_safe is False
    assert result.requires_human_review is True
    assert result.violation_type == ViolationType.HATE_SPEECH


@pytest.mark.asyncio
async def test_explicit_violence_is_blocked_by_primary_moderation(service: ModerationService):
    result = await moderate(service, "I want to kill and murder everyone in this attack.")

    assert result.decision == ModerationDecision.BLOCK
    assert result.is_safe is False
    assert result.requires_human_review is False
    assert result.violation_type == ViolationType.VIOLENCE
    assert result.provider == "openai"
    assert "high confidence" in result.reasoning.lower()
