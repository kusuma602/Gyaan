import pytest


from gyaan_auth.storages.storage_implementation import StorageImplementation


class TestGetListofUserDTOS:

    @pytest.mark.django_db
    def test_with_all_valid_users_returns_all_user_ids(self, create_users):
        # Arrange
        user_ids = [1, 2, 3]

        sql_storage = StorageImplementation()

        # Act
        response = sql_storage.get_valid_user_ids(
            user_ids=user_ids
        )

        # Assert
        assert response == user_ids

    @pytest.mark.django_db
    def test_with_some_valid_users_returns_valid_user_ids(self, create_users):
        # Arrange
        user_ids = [1, 2, 3, 5, 10, 11]
        valid_user_ids = [1, 2, 3, 5]
        sql_storage = StorageImplementation()

        # Act
        response = sql_storage.get_valid_user_ids(
            user_ids=user_ids
        )

        # Assert
        assert response == valid_user_ids

    @pytest.mark.django_db
    def test_with_all_invalid_values_returns_empty_list(self, create_users):
        # Arrange
        user_ids = [10, 11, 12]
        valid_user_ids = []
        sql_storage = StorageImplementation()

        # Act
        response = sql_storage.get_valid_user_ids(
            user_ids=user_ids
        )

        # Assert
        assert response == valid_user_ids