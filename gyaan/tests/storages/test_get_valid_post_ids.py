import pytest


from gyaan.storages.storage_implementation import \
        StorageImplementation


class TestGetValidPostIDs:

    @pytest.mark.django_db
    def test_with_valid_post_ids_returns_all_post_ids(self,
                                                      create_domain_posts):

        # Arrange
        post_ids = [1, 2, 3, 4]
        sql_storage = StorageImplementation()
        expected_response = [1, 2, 3, 4]

        # Act
        response = sql_storage.get_valid_post_ids(post_ids=post_ids)

        # Assert
        assert response == expected_response

    @pytest.mark.django_db
    def test_with_all_invalid_domain_ids_returns_empty_list(
            self,
            create_domain_posts):

        # Arrange
        post_ids = [5, 6, 7, 8]
        sql_storage = StorageImplementation()
        expected_response = []

        # Act
        response = sql_storage.get_valid_post_ids(post_ids=post_ids)

        # Assert
        assert response == expected_response

    @pytest.mark.django_db
    def test_with_list_of_valid_and_invalid_post_ids_returns_valid_post_ids(
            self,
            create_domain_posts):

        # Arrange
        post_ids = [1, 2, 3, 5, 6, 7, 8]
        sql_storage = StorageImplementation()
        expected_response = [1, 2, 3]

        # Act
        response = sql_storage.get_valid_post_ids(post_ids=post_ids)

        # Assert
        assert response == expected_response
