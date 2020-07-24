from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class DomainDTO:
    domain_id: int
    domain_name: str
    description: str


@dataclass
class PostDTO:
    post_id: int
    title: str
    description: str
    posted_at: datetime
    posted_by_id: int
    domain_id: int


@dataclass
class ReactionDTO:
    from gyaan.constants.enums import ReactionChoices
    reaction_id: int
    reaction: ReactionChoices
    reacted_by_id: int
    post_id: Optional[int]
    comment: Optional[int]
    reacted_at: datetime


@dataclass
class CommentDTO:
    comment_id: int
    commented_by_id: int
    commented_at: datetime
    comment_content: str
    post_id: int
    comment_id: Optional[int]


@dataclass
class PostCommentsCountDTO:
    post_id: int
    comments_count: int


@dataclass
class PostReactionsCountDTO:
    post_id: int
    reactions_count: int


@dataclass
class CommentReactionsCountDTO:
    comment_id: int
    reactions_count: int


@dataclass
class TagDTO:
    tag_id: int
    tag_name: str


@dataclass
class PostTagDTO:
    post_id: int
    tag_id: int


@dataclass
class CommentRepliesCountDTO:
    comment_id: int
    replies_count: int
