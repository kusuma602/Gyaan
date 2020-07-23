from gyaan.exceptions.custom_exceptions import InvalidDomainID
from gyaan.interactors.dtos import CompleteDomainDetailsDTO
from gyaan.interactors.mixins.get_user_dtos import GetUserDtosMixin
from gyaan.interactors.presenters.presenter_interface import \
    GetDomainDetailsPresenterInterface
from gyaan.interactors.storages.storage_interface import \
    StorageInterface


class GetDomainDetailsInteractor(GetUserDtosMixin):
    def __init__(self, storage: StorageInterface):
        self.storage = storage

    # def get_domain_details_wrapper(
    #         self,
    #         domain_id: int,
    #         presenter: GetDomainDetailsPresenterInterface):
    #     try:
    #         response = self.get_domain_details_response(
    #             domain_id=domain_id,
    #             presenter=presenter
    #         )
    #     except InvalidDomainID:
    #         response = presenter.raise_invalid_domain_id_exception()
    #
    #     return response
    #
    # def get_domain_details_response(
    #         self,
    #         domain_id: int,
    #         presenter: GetDomainDetailsPresenterInterface):
    #
    #     domain_details_dto = self.get_domain_details(domain_id=domain_id)
    #     response = presenter.get_domain_details_response

    def get_domain_details(self, domain_id: int) -> CompleteDomainDetailsDTO:
        self.storage.validate_domain_id(domain_id=domain_id)
        domain_dto = self.storage.get_domain_dto(domain_id=domain_id)
        posts_count = self.storage.get_domain_posts_count(domain_id=domain_id)
        members_count = self.storage.get_domain_members_count(
            domain_id=domain_id
        )
        expert_ids = self.storage.get_domain_experts_ids(
            domain_id=domain_id
        )
        book_marks_count = self.storage.get_domain_book_marks_count(
            domain_id=domain_id
        )
        domain_expert_dtos = self.get_user_dtos(user_ids=expert_ids)
        return CompleteDomainDetailsDTO(
            domain_dto=domain_dto,
            domain_posts_count=posts_count,
            domain_members_count=members_count,
            book_marks_count=book_marks_count,
            domain_expert_dtos=domain_expert_dtos
        )
