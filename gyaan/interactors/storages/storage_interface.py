from abc import ABC
from abc import abstractmethod


from gyaan.storages.dtos import Domain_DTO


class StorageInterface(ABC):

    @abstractmethod
    def validate_domain_id(self, domain_id: int):
        pass

    @abstractmethod
    def get_domain_dto(self, domain_id: int) -> Domain_DTO:
        pass