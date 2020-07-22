import pytest

from gyaan_auth.storages.dtos import UserDTO
from gyaan_auth.storages.storage_implementation import StorageImplementation


class TestGetListofUserDTOS:

    @pytest.mark.django_db
    def test_with_user_ids_returns_list_of_user_dtos(self, create_users):
        # Arrange
        user_ids = [1, 2, 3]
        expected_response = [
            UserDTO(
                user_id=1,
                name='user_1',
                is_admin=False,
                is_domain_expert=False),
            UserDTO(
                user_id=2,
                name='user_2',
                is_admin=False,
                is_domain_expert=False),
            UserDTO(
                user_id=3,
                name='user_3',
                is_admin=False,
                is_domain_expert=False),
         ]

        sql_storage = StorageImplementation()

        # Act
        response = sql_storage.get_list_of_user_dtos(
            user_ids=user_ids
        )

        # Assert
        assert response == expected_response
