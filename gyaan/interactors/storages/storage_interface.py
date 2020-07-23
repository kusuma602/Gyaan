from abc import ABC
from abc import abstractmethod
from typing import List

from gyaan.storages.dtos import DomainDTO


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
