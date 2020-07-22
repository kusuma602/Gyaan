from typing import List

from gyaan_auth.interactors.storage_interfaces.storage_interface import \
    StorageInterface
from gyaan_auth.interactors.presenter_interfaces.presenter_interface import \
    GetUserDtoPresenterInterface


class GetUserDtosInteractor:
    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def get_user_dtos_wrapper(self,
                              presenter: GetUserDtoPresenterInterface,
                              user_ids: List[int]):
        from gyaan_auth.exceptions.custom_exceptions import InvalidUserIds

        try:
            response =  self.get_user_dtos(user_ids=user_ids)
        except InvalidUserIds as err:
            response = presenter.raise_invalid_user_ids_exception(err)

        return response

    def get_user_dtos(self, user_ids: List[int]):
        from gyaan_auth.exceptions.custom_exceptions import InvalidUserIds
        unique_user_ids = list(set(user_ids))
        valid_user_ids = self.storage.get_valid_user_ids(
            user_ids=unique_user_ids
        )
        invalid_user_ids = [
            user_id
            for user_id in user_ids
            if user_id not in valid_user_ids
        ]
        if invalid_user_ids:
            raise InvalidUserIds(invalid_user_ids=invalid_user_ids)
        user_dtos = self.storage.get_list_of_user_dtos(user_ids=valid_user_ids)
        return user_dtos
