import pytest


from gyaan.storages.storage_implementation import \
        StorageImplementation


class TestGetLatestCommentIDs:

    @pytest.mark.django_db
    def test_with_post_ids_returns_latest_comment_ids(
            self,
            create_comments):

        # Arrange
        post_id = 1
        number_of_comments = 2
        sql_storage = StorageImplementation()
        expected_response = [1, 2]

        # Act
        response = sql_storage.get_latest_comment_ids(
                post_id=post_id, no_of_comments=number_of_comments
            )

        # Assert
        assert response == expected_response
