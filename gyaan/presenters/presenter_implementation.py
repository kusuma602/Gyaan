import json
from typing import Dict

from django.http import HttpResponse, response

from gyaan.constants.exception_messages import INVALID_POST_IDS
from gyaan.interactors.presenters.presenter_interface import \
    GetDomainDetailsPresenterInterface, GetPostsPresenterInterface


class GetDomainDetailsPresenterImplementation(GetDomainDetailsPresenterInterface):

    def get_invalid_domain_id_response(self) -> HttpResponse:

        from gyaan.constants.exception_messages import INVALID_DOMAIN_ID
        data = json.dumps({
            "response": INVALID_DOMAIN_ID[0],
            "http_status_code": 400,
            "res_status": INVALID_DOMAIN_ID[1]
        })
        response_object = response.HttpResponse(data, status=400)
        return response_object

    def get_domain_details_response(self, domain_details_dto) -> HttpResponse:
        domain_dto = domain_details_dto.domain_dto
        expert_dtos = domain_details_dto.domain_expert_dtos
        expert_details_dict = []
        for expert_dto in expert_dtos:
            expert_details = expert_dto.__dict__
            expert_details_dict.append(expert_details)

        domain_details_dict = {
            'domain_name': domain_dto.domain_name,
            'description': domain_dto.description,
            'domain_members_count': domain_details_dto.domain_members_count,
            'domain_posts_count': domain_details_dto.domain_posts_count,
            'domain_book_marks_count': domain_details_dto.book_marks_count,
            'domain_experts': expert_details_dict
        }
        data = json.dumps(domain_details_dict)
        response_object = response.HttpResponse(data, status=400)
        return response_object


class GetPostsPresenterImplementation(GetPostsPresenterInterface):

    def return_invalid_posts_response(self, err_obj) -> HttpResponse:
        invalid_post_ids = err_obj.invalid_post_ids
        invalid_post_ids_response = \
            f"{INVALID_POST_IDS[0]} Invalid user ids: {invalid_post_ids}"

        data = json.dumps({
            "response": invalid_post_ids_response,
            "http_status_code": 400,
            "res_status": INVALID_POST_IDS[1]
        })
        response_object = response.HttpResponse(data, status=400)
        return response_object

    def get_posts_response(self, complete_post_dtos) -> HttpResponse:
        posts_list = []
        post_dtos = complete_post_dtos.post_dtos
        for post_dto in post_dtos:
            post_dict = self._preapre_post_dictionary(post_dto, complete_post_dtos)
            posts_list.append(post_dict)

    def _preapre_post_dictionary(self, post_dto, complete_post_dtos) -> Dict:
        comment_dtos = complete_post_dtos.comment_dtos
        post_comments_count_dto = complete_post_dtos.post_comments_count_dto
        post_reactions_count_dto = complete_post_dtos.post_reactions_count_dto
        comment_reactions_count_dto = complete_post_dtos.comment_reactions_count_dto
        comment_replies_counts = complete_post_dtos.comment_replies_counts
        user_dtos = complete_post_dtos.user_dtos

        post_id = post_dto.post_id
        reactions_count = self._get_post_reactions_count(
            post_id, post_reactions_count_dto
        )
        comments_count = self._get_post_comments_count(
            post_comments_count_dto, post_id
        )

    @staticmethod
    def _get_post_comments_count(post_comments_count_dto, post_id) -> int:
        for post_comment_dto in post_comments_count_dto:
            is_post_comment = post_comment_dto.post_id == post_id
            if is_post_comment:
                comments_count = post_comment_dto.comments_count
        return comments_count

    @staticmethod
    def _get_post_reactions_count(post_id, post_reactions_count_dto) -> int:
        for post_reactions_dto in post_reactions_count_dto:
            is_post_reactions_count = post_reactions_dto.post_id == post_id
            if is_post_reactions_count:
                reactions_count = post_reactions_dto.reactions_count
        return reactions_count

    @staticmethod
    def _get_post_Comments(self, post_id, comment_dtos):
        comments_list = []
        for comment_dto in comment_dtos:
            is_post_direct_comment = comment_dto.post_id == post_id and comment_dto.parent_comment_id is None
            if is_post_direct_comment:
                comments_list.append(is_post_direct_comment)
        return comments_list



