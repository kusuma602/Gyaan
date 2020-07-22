import pytest

from gyaan_auth.storages.storage_implementation import StorageImplementation


class TestGetUserDTO:

    @pytest.mark.django_db
    def test_with_invalid_user_id_raises_exception(self, create_users):
        from gyaan_auth.exceptions import InvalidUserID

        # Arrange
        user_id = 15
        sql_storage = StorageImplementation()

        # Act
        with pytest.raises(InvalidUserID):
            sql_storage.get_user_dto(user_id=user_id)

    @pytest.mark.django_db
    def test_with_valid_user_id_raises_exception(self, create_users):
        from gyaan_auth.tests.factories.storage_dtos import UserDTO

        # Arrange
        user_id = 1
        sql_storage = StorageImplementation()
        expected_response = UserDTO(
            user_id=1,
            name="user_1",
            is_admin=False,
            is_domain_expert=False
        )

        # Act
        response = sql_storage.get_user_dto(user_id=user_id)

        # Assert
        assert response == expected_response
