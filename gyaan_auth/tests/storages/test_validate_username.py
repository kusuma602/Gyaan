import pytest


from gyaan_auth.storages.storage_implementation import StorageImplementation


class TestValidateUsername:

    @pytest.mark.django_db
    def test_with_invalid_username_raises_exception(self, create_users):

        # Arrange
        from gyaan_auth.exceptions import InvalidUsername
        sql_storage = StorageImplementation()
        username = "username"

        # Act
        with pytest.raises(InvalidUsername):
            sql_storage.validate_username(username=username)

    @pytest.mark.django_db
    def test_with_valid_username_returns_none(self, create_users):

        # Arrange
        sql_storage = StorageImplementation()
        username = "username_1"

        # Act
        sql_storage.validate_username(username=username)
