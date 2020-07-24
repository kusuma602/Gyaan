from abc import ABC
from abc import abstractmethod
from dataclasses import dataclass
from typing import List

from django.http import HttpResponse

from gyaan.adapters.dtos import UserDTO
from gyaan.storages.dtos import PostDTO, CommentDTO, CommentRepliesCountDTO, CommentReactionsCountDTO, \
    PostReactionsCountDTO, PostCommentsCountDTO


class GetDomainDetailsPresenterInterface(ABC):

    @abstractmethod
    def raise_invalid_domain_id_exception(self):
        pass


class GetPostsPeresenterInterface(ABC):

    @abstractmethod
    def return_invalid_posts_response(self, err_obj) -> HttpResponse:
        pass

    @abstractmethod
    def get_posts_response(self, post_dto) -> HttpResponse:
        pass