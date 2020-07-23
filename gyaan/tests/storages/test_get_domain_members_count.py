import pytest

from gyaan.storages.storage_implementation import StorageImplementation


class TestGetDomainMembersCount:
    @pytest.mark.django_db
    def test_when_domain_members_in_db_returns_members_count(
            self,
            create_domain_members):

        sql_storage = StorageImplementation()

        # Arrange
        domain_id = 1
        expected_response = 3

        # Act
        response = sql_storage.get_domain_members_count(domain_id=domain_id)

        # Assert
        assert response == expected_response

    @pytest.mark.django_db
    def test_when_no_domain_members_in_db_returns_zero(self,
                                                     create_domain_members):
        sql_storage = StorageImplementation()

        # Arrange
        domain_id = 10
        expected_response = 0

        # Act
        response = sql_storage.get_domain_members_count(domain_id=domain_id)

        # Assert
        assert response == expected_response
