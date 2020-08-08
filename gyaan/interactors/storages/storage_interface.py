from abc import ABC
from abc import abstractmethod
from typing import List

from gyaan.storages.dtos import DomainDTO, PostDTO, CommentDTO, \
    PostCommentsCountDTO, CommentReactionsCountDTO, \
    CommentRepliesCountDTO, PostReactionsCountDTO, PostTagDTO


class StorageInterface(ABC):

    @abstractmethod
    def validate_domain_id(self, domain_id: int):
        pass

    @abstractmethod
    def get_domain_dto(self, domain_id: int) -> DomainDTO:
        pass

    @abstractmethod
    def get_domain_posts_count(self, domain_id: int) -> int:
        pass

    @abstractmethod
    def get_domain_members_count(self, domain_id: int) -> int:
        pass

    @abstractmethod
    def get_domain_experts_ids(self, domain_id: int) -> List[int]:
        pass

    @abstractmethod
    def get_domain_book_marks_count(self, domain_id: int) -> int:
        pass

    @abstractmethod
    def get_valid_post_ids(self, post_ids: List[int]) -> List[int]:
        pass

    @abstractmethod
    def get_post_dtos(self, post_ids: List[int]) -> List[PostDTO]:
        pass

    @abstractmethod
    def get_post_reactions_counts(self, post_ids: List[int]) -> List[PostReactionsCountDTO]:
        pass

    @abstractmethod
    def get_latest_comment_ids(
            self, post_id: int, no_of_comments:int) -> List[int]:
        pass

    @abstractmethod
    def get_comment_dtos(self, comment_ids: List[int]) -> List[CommentDTO]:
        pass

    @abstractmethod
    def get_comment_replies_count(self, comment_ids: List[int]) -> List[CommentRepliesCountDTO]:
        pass

    @abstractmethod
    def get_comment_reactions_count(self, comment_ids: List[int]) -> List[CommentReactionsCountDTO]:
        pass

    @abstractmethod
    def get_post_comments_count(self, post_ids: List[int]) -> List[PostCommentsCountDTO]:
        pass

    @abstractmethod
    def get_post_tag_dto(self, post_id: int) -> PostTagDTO:
        pass
