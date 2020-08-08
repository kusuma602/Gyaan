from abc import ABC
from abc import abstractmethod


from django.http import HttpResponse


class GetDomainDetailsPresenterInterface(ABC):

    @abstractmethod
    def get_invalid_domain_id_response(self)-> HttpResponse:
        pass

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


class GetDomainPostsPresenterInterface(ABC):

    @abstractmethod


    @abstractmethod
    def