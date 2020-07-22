from abc import ABC
from abc import abstractmethod
from typing import List

from gyaan_auth.storages.dtos import UserDTO


class StorageInterface(ABC):

    @abstractmethod
    def validate_username(self, username: str):
        pass

    @abstractmethod
    def validate_password(self, username: str, password: str):
        pass

    @abstractmethod
    def get_user_dto(self, user_id: int) -> UserDTO:
        pass

    @abstractmethod
    def get_valid_user_ids(self, user_ids: List[int]) -> List[int]:
        pass

    @abstractmethod
    def get_list_of_user_dtos(self, user_ids: List[int]) -> List[UserDTO]:
        pass
