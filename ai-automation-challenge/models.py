from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum

class ViolationType(str, Enum):
    HATE_SPEECH = "hate_speech"
    VIOLENCE = "violence"
    ADULT_CONTENT = "adult_content"
    SPAM = "spam"
    NONE = "none"

class ModerationRequest(BaseModel):
    """Request model for content moderation"""
    content: str = Field(..., min_length=1)
    creator_id: str
    video_id: Optional[str] = None

class ModerationDecision(str, Enum):
    ALLOW = "allow"
    REVIEW = "review"
    BLOCK = "block"

class ModerationResult(BaseModel):
    """Structured AI moderation result"""
    decision: ModerationDecision
    is_safe: bool
    requires_human_review: bool = False
    confidence: float = Field(..., ge=0.0, le=1.0)
    violation_type: ViolationType
    reasoning: str
    provider: str  # "openai", "anthropic", or "openai+anthropic"

class ModerationResponse(BaseModel):
    """API response model"""
    video_id: Optional[str]
    moderation: ModerationResult
    processing_time_ms: float
