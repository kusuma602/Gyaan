from dataclasses import dataclass
from typing import List


from gyaan.adapters.dtos import UserDTO
from gyaan.storages.dtos import PostDTO, CommentDTO, \
    PostCommentsCountDTO, PostReactionsCountDTO, \
    CommentReactionsCountDTO, CommentRepliesCountDTO


@dataclass
class CompletePostDetailsDTO:
    post_dtos: List[PostDTO]
    comment_dtos: List[CommentDTO]
    post_comments_count_dto: List[PostCommentsCountDTO]
    post_reactions_count_dto: List[PostReactionsCountDTO]
    comment_reactions_count_dto: List[CommentReactionsCountDTO]
    comment_replies_counts: List[CommentRepliesCountDTO]
    user_dtos: List[UserDTO]
