import pytest


from gyaan.storages.storage_implementation import \
        StorageImplementation


class TestGetPostDTOs:

    @pytest.mark.django_db
    def test_with_valid_post_ids_returns_post_dtos(self,
                                                   create_domain_posts,
                                                   create_post_dto_factories):

        # Arrange
        post_ids = [1, 2, 3, 4]
        sql_storage = StorageImplementation()
        expected_response = create_post_dto_factories

        # Act
        response = sql_storage.get_post_dtos(post_ids=post_ids)

        # Assert
        assert response == expected_response
