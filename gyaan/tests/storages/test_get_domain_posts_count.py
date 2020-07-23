import pytest

from gyaan.storages.storage_implementation import StorageImplementation


class TestGetDomainPostsCount:
    @pytest.mark.django_db
    def test_when_domain_posts_in_db_returns_posts_count(self,
                                                       create_domain_posts):
        sql_storage = StorageImplementation()

        # Arrange
        domain_id = 1
        expected_response = 1

        # Act
        response = sql_storage.get_domain_posts_count(domain_id=domain_id)

        # Assert
        assert response == expected_response

    @pytest.mark.django_db
    def test_when_no_domain_posts_in_db_returns_zero(self,
                                                       create_domain_posts):
        sql_storage = StorageImplementation()

        # Arrange
        domain_id = 10
        expected_response = 0

        # Act
        response = sql_storage.get_domain_posts_count(domain_id=domain_id)

        # Assert
        assert response == expected_response

