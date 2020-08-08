from django.http import HttpResponse

from gyaan.exceptions.custom_exceptions import UserNotDomainMember, InvalidDomainID
from gyaan.interactors.storages.storage_interface import StorageInterface


class GetDomainPosts:
    def __init__(self, storage: StorageInterface):
        self.storage = storage
    def get_domain_posts_wrapper(self,
                                 user_id: int,
                                 presenter: GetDomainPostsPresenterInterface,
                                 offset: int,
                                 limit: int,
                                 domain_id: int) -> HttpResponse:
        try:
            response = self._get_domain_posts_response(
                user_id=user_id,
                domain_id=domain_id,
                offset=offset,
                limit=limit,
                presenter=presenter
            )
        except UserNotDomainMember:
            response = presenter.get_user_not_domain_member_response()
        except InvalidDomainID:
            response = presenter.get_invalid_domain_id_response()
        return response

    def _get_domain_posts_response(
            self,
            user_id: int,
            domain_id: int,
            offset: int,
            limit: int,
            presenter: GetDomainPostsPresenterInterface) -> HttpResponse:
        posts_complete_details_dto = self.get_domain_posts(
            user_id=user_id,
            domain_id=domain_id,
            offset=offset,
            limit=limit,
            presenter=presenter
        )
        presenter.get_domain_posts_response(posts_complete_dto=posts_complete_dto)

    def get_domain_posts(self, user_id, domain_id, offset, limit, presenter) -> List[CompletePostDetailsDTO]:
        self.storage.validate_domain_id(domain_id)
        self.storage.validate_domain_user(
            user_id=user_id,
            domain_id=domain_id
        )
        post_ids = self.storage.get_domain_post_ids(
            domain_id=domain_id,
            offset=offset,
            limit=limit
        )
        from gyaan.interactors.get_posts_interactor import GetPostsInteractor
        get_posts_interactor = GetPostsInteractor(
            storage=self.storage
        )
