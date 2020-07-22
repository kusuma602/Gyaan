from typing import List

from gyaan_auth.interactors.storage_interfaces.storage_interface import \
    StorageInterface
from gyaan_auth.storages.dtos import UserDTO


class StorageImplementation(StorageInterface):

    def validate_username(self, username: str):
        from gyaan_auth.models import User
        from gyaan_auth.exceptions import InvalidUsername

        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            raise InvalidUsername

    def validate_password(self, username: str, password: str):
        from gyaan_auth.models import User
        from gyaan_auth.exceptions import InvalidPassword

        user_obj = User.objects.get(username=username)
        is_password_valid = user_obj.check_password(password)
        is_password_not_valid = not is_password_valid
        if is_password_not_valid:
            raise InvalidPassword

        return user_obj.id

    def get_user_dto(self, user_id: int) -> UserDTO:
        from gyaan_auth.models import User
        from gyaan_auth.exceptions import InvalidUserID

        try:
            user_obj = User.objects.get(id=user_id)
        except User.DoesNotExist:
            raise InvalidUserID

        return UserDTO(
            user_id=user_obj.id,
            name=user_obj.name,
            is_admin=user_obj.is_admin,
            is_domain_expert=user_obj.is_domain_expert
        )

    def get_list_of_user_dtos(self, user_ids: List[int]) -> List[UserDTO]:
        user_dtos = []
        for user_id in user_ids:
            user_dto = self.get_user_dto(user_id=user_id)
            user_dtos.append(user_dto)
        return user_dtos

    def get_valid_user_ids(self, user_ids: List[int]) -> List[int]:
        from gyaan_auth.models import User
        user_ids_in_db = User.objects.all().values_list('id', flat=True)
        valid_user_ids = []
        for user_id in user_ids:
            if user_id in user_ids_in_db:
                valid_user_ids.append(user_id)
        return valid_user_ids
