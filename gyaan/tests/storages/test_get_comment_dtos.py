import pytest


from gyaan.storages.storage_implementation import \
        StorageImplementation


class TestGetCommentDTOs:

    @pytest.mark.django_db
    def test_with_comment_ids_returns_comment_dtos(self,
                                                   create_comments,
                                                   create_comment_dtos):

        # Arrange
        comment_ids = [1, 2, 3, 4]
        sql_storage = StorageImplementation()
        expected_response = create_comment_dtos

        # Act
        response = sql_storage.get_comment_dtos(comment_ids=comment_ids)

        # Assert
        assert response == expected_response
