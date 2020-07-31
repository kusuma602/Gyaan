from abc import ABC
from abc import abstractmethod


from django.http import HttpResponse, response


class GetDomainDetailsPresenterInterface(ABC):

    def get_invalid_domain_id_response(self) -> HttpResponse:
        import json
        from gyaan.constants.exception_messages import INVALID_DOMAIN_ID
        data = json.dumps({
            "response": INVALID_DOMAIN_ID[0],
            "http_status_code": 400,
            "res_status": INVALID_DOMAIN_ID[1]
        })
        response_object = response.HttpResponse(data, status=400)
        return response_object

    @abstractmethod
    def get_domain_details_response(self, domain_details_dto) -> HttpResponse:
        pass


class GetPostsPresenterInterface(ABC):

    @abstractmethod
    def return_invalid_posts_response(self, err_obj) -> HttpResponse:
        pass

    @abstractmethod
    def get_posts_response(self, post_dto) -> HttpResponse:
        pass