from typing import List

from django.http import HttpResponse

from gyaan.adapters.dtos import UserDTO
from gyaan.interactors.dtos import PostDetailsDTO, CommentDeatilsDTO
from gyaan.interactors.mixins.get_user_dtos import GetUserDtosMixin
from gyaan.interactors.presenters.dtos import CompletePostDetailsDTO
from gyaan.interactors.presenters.presenter_interface import \
    GetPostsPeresenterInterface
from gyaan.interactors.storages.storage_interface import StorageInterface


class GetPostsInteractor(GetUserDtosMixin):

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def get_posts_wrapper(self,
                          presenter: GetPostsPeresenterInterface,
                          post_ids: List[int]) -> HttpResponse:

        from gyaan.exceptions.custom_exceptions import InvalidPostIds
        try:
            response = self.get_posts_response(presenter=presenter, post_ids=post_ids)
        except InvalidPostIds as err:
            response = presenter.return_invalid_posts_response(err)

        return response

    def get_posts_response(self,
                           presenter: GetPostsPeresenterInterface,
                           post_ids: List[int]) -> HttpResponse:
        post_dtos = self.get_posts(post_ids=post_ids)
        response = presenter.get_posts_response(post_dto=post_dtos)
        return response

    def get_posts(self, post_ids: List[int]) -> CompletePostDetailsDTO:
        unique_post_ids = list(set(post_ids))
        self._validate_post_ids(post_ids=unique_post_ids)
        post_details_dto = self._get_post_details(unique_post_ids)
        comment_details_dto = self._get_comment_details(unique_post_ids)
        user_dtos = self._get_user_dtos(
            post_comments_dtos=comment_details_dto.post_comments_dtos,
            post_dtos=post_details_dto.post_dtos
        )
        return CompletePostDetailsDTO(
            post_dtos=post_details_dto.post_dtos,
            comment_dtos=comment_details_dto.post_comments_dtos,
            post_comments_count_dto=post_details_dto.post_comments_count,
            post_reactions_count_dto=post_details_dto.post_reactions_count,
            comment_reactions_count_dto=comment_details_dto.comment_reactions_count,
            comment_replies_counts=comment_details_dto.comment_replies_count,
            user_dtos=user_dtos
        )

    def _get_comment_details(self, unique_post_ids) -> CommentDeatilsDTO:
        comment_ids = self._get_latest_comment_ids(
            post_ids=unique_post_ids
        )
        post_comments_dtos = self.storage.get_comment_dtos(
            comment_ids=comment_ids
        )
        comment_replies_count = self.storage.get_comment_replies_count(
            comment_ids=comment_ids
        )
        comment_reactions_count = self.storage.get_comment_reactions_count(
            comment_ids=comment_ids
        )
        return CommentDeatilsDTO(
            comment_reactions_count=comment_reactions_count,
            comment_replies_count=comment_replies_count,
            post_comments_dtos=post_comments_dtos
        )

    def _get_post_details(self, unique_post_ids) -> PostDetailsDTO:
        post_dtos = self.storage.get_post_dtos(post_ids=unique_post_ids)
        post_reactions_count = self.storage.get_post_reactions_count(
            post_ids=unique_post_ids
        )
        post_comments_count = self.storage.get_post_comments_count(
            post_ids=unique_post_ids
        )
        return PostDetailsDTO(
            post_comments_count=post_comments_count,
            post_dtos=post_dtos,
            post_reactions_count=post_reactions_count
        )

    def _get_user_dtos(self, post_comments_dtos, post_dtos) -> List[UserDTO]:
        user_ids = [post_dto.posted_by_id for post_dto in post_dtos]
        user_ids += [
            comment_dto.commented_by_id for comment_dto in post_comments_dtos
        ]
        user_dtos = self.get_user_dtos(user_ids=user_ids)
        return user_dtos

    def _validate_post_ids(self, post_ids):
        unique_post_ids = list(set(post_ids))
        valid_post_ids = self.storage.get_valid_post_ids(
            post_ids=unique_post_ids
        )
        invalid_post_ids = [
            post_id for post_id in unique_post_ids
            if post_id not in valid_post_ids
        ]
        if invalid_post_ids:
            from gyaan.exceptions.custom_exceptions import InvalidPostIds
            raise InvalidPostIds(invalid_post_ids=invalid_post_ids)

    def _get_latest_comment_ids(self, post_ids):
        comment_ids = []
        for post_id in post_ids:
            comment_ids += self.storage.get_latest_comment_ids(
                post_id=post_id, no_of_comments=2
            )
        return comment_ids
