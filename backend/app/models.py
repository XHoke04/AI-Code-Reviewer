from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, JSON
from sqlalchemy.sql import func
from app.database import Base

class PullRequestReview(Base):
    """Model for storing PR review data."""
    
    __tablename__ = "pull_request_reviews"

    # Primary key
    id = Column(Integer, primary_key=True, index=True)

    # Github PR info
    repo_owner = Column(String(255), nullable=False, index=True)
    repo_name = Column(String(255), nullable=False, index=True)
    pr_number = Column(Integer, nullable=False, index=True)
    pr_title = Column(String(500))
    pr_author = Column(String(255))

    # Review data
    files_changed = Column(JSON)
    review_comments = Column(Text) # AI generated review
    ai_model = Column(String(100), default="gpt-4") # model used

    # Metadata
    status = Column(String(50), default="pending") # pending, completed, failed
    error_message = Column(Text, nullable=True)

    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    def __repr__(self):
        return f"<PullRequestReview(id={self.id}, repo={self.repo_owner}/{self.repo_name}, pr={self.pr_number})>"
    
class ReviewComment(Base):
    """Model for individual review comments on specific files/lines."""

    __tablename__ = "review_comments"

    # Primary key
    id = Column(Integer, primary_key=True, index=True)

    # Link to PR review
    pr_review_id = Column(Integer, index=True)

    # Comment details
    file_path = Column(String(500), nullable=False)
    line_number = Column(Integer, nullable=True)
    comment_text = Column(Text, nullable=False)
    severity = Column(String(50)) # suggesting, warning, error

    # Was this posted to Github?
    posted_to_github = Column(Boolean, default=False)
    github_comment_id = Column(Integer, nullable=True)

    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return f"<ReviewComment(id={self.id}, file={self.file_path}, line={self.line_number})>"