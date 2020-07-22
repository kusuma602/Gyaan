from typing import List

from gyaan_auth.interactors.get_user_dtos import \
    GetUserDtosInteractor
from gyaan_auth.storages.dtos import UserDTO
from gyaan_auth.storages.storage_implementation import StorageImplementation


class ServiceInterface:

    @staticmethod
    def get_user_dtos(user_ids: List[int]) -> List[UserDTO]:
        storage = StorageImplementation()
        interactor = GetUserDtosInteractor(storage=storage)
        user_dtos = interactor.get_user_dtos(user_ids=user_ids)
        return user_dtos