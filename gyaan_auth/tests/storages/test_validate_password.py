import pytest


from gyaan_auth.storages.storage_implementation import StorageImplementation


class TestValidatePassword:

    @pytest.mark.django_db
    def test_with_invalid_password_raises_exception(self, create_users):

        # Arrange
        from gyaan_auth.exceptions import InvalidPassword
        sql_storage = StorageImplementation()
        username = "username_1"
        password = "invalid password"

        # Act
        with pytest.raises(InvalidPassword):
            sql_storage.validate_password(username=username, password=password)

    @pytest.mark.django_db
    def test_with_valid_password_returns_user_id(self, create_users):

        # Arrange
        sql_storage = StorageImplementation()
        username = "username_1"
        password = "password"
        expected_response = 1

        # Act
        response = sql_storage.validate_password(
            username=username,
            password=password
        )

        # Assert
        assert response == expected_response
