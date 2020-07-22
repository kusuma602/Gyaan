from gyaan.exceptions.custom_exceptions import InvalidDomainID
from gyaan.interactors.presenters.presenter_interface import \
    GetDomainDetailsPresenterInterface
from gyaan.interactors.storages.storage_interface import \
    StorageInterface


class GetDomainDetailsInteractor:
    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def get_domain_details_wrapper(
            self,
            domain_id: int,
            presenter: GetDomainDetailsPresenterInterface):
        try:
            response =  self.get_domain_details_response(
                domain_id=domain_id,
                presenter=presenter
            )
        except InvalidDomainID:
            response = presenter.raise_invalid_domain_id_exception()

        return response

    def get_domain_details_response(
            self,
            domain_id: int,
            presenter: GetDomainDetailsPresenterInterface) -> int:

        self.get_domain_details(domain_id=domain_id)

    def get_domain_details(self, domain_id: int):
        self.storage.validate_domain_id(domain_id=domain_id)
        domain_dto = self.storage.get_domain_dto(domain_id=domain_id)

        return domain_dto