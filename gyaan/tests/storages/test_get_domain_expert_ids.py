import pytest

from gyaan.storages.storage_implementation import StorageImplementation


class TestGetDomainExpertIds:
    @pytest.mark.django_db
    def test_when_in_domain_experts_db_returns_members_count(
            self,
            create_domain_experts):

        sql_storage = StorageImplementation()

        # Arrange
        domain_id = 1
        expected_response = [1, 2, 3]

        # Act
        response = sql_storage.get_domain_experts_ids(domain_id=domain_id)

        # Assert
        assert response == expected_response

    @pytest.mark.django_db
    def test_when_no_domain_experts_in_db_returns_zero(self,
                                                       create_domains,
                                                       create_domain_experts):
        sql_storage = StorageImplementation()

        # Arrange
        domain_id = 10
        expected_response = []

        # Act
        response = sql_storage.get_domain_experts_ids(domain_id=domain_id)

        # Assert
        assert response == expected_response
