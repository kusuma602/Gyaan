from dataclasses import dataclass
from typing import List


from gyaan.storages.dtos import DomainDTO, PostDTO, \
    PostCommentsCountDTO, PostReactionsCountDTO, \
    CommentReactionsCountDTO, CommentRepliesCountDTO, CommentDTO
from gyaan_auth.storages.dtos import UserDTO


@dataclass
class CompleteDomainDetailsDTO:
    domain_dto: DomainDTO
    domain_posts_count: int
    domain_members_count: int
    book_marks_count: int
    domain_expert_dtos: List[UserDTO]


@dataclass
class PostDetailsDTO:
    post_dtos: List[PostDTO]
    post_comments_count: List[PostCommentsCountDTO]
    post_reactions_count:  List[PostReactionsCountDTO]


@dataclass
class CommentDeatilsDTO:
    comment_reactions_count: List[CommentReactionsCountDTO]
    comment_replies_count: List[CommentRepliesCountDTO]
    post_comments_dtos: List[CommentDTO]
