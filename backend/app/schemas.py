from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class ReviewCommentBase(BaseModel):
    """Base schema for review comments"""
    file_path: str
    line_number: Optional[int] = None
    comment_text: str
    severity: str = "suggestion"

class ReviewCommentCreate(ReviewCommentBase):
    """Schema for creating a review comment."""
    pass

class ReviewComment(ReviewCommentBase):
    """Schema for review comment response."""
    id: int
    pr_review_id: int
    posted_to_github: bool
    created_at: datetime

    class Config:
        from_attributes = True

class PullRequestReviewBase(BaseModel):
    """Base schema for pull request reviews."""
    repo_owner: str
    repo_name: str
    pr_number: int
    pr_title: Optional[str] = None
    pr_author: Optional[str] = None

class PullRequestReviewCreate(PullRequestReviewBase):
    """Schema for creating a PR review."""
    pass

class PullRequestReview(PullRequestReviewBase):
    """Schema for PR review response."""
    id: int
    files_changed: Optional[dict] = None
    review_comments: Optional[str] = None
    ai_model: str
    status: str
    error_message: Optional[str] = None
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True