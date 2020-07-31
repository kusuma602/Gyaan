import pytest


from gyaan.storages.storage_implementation import \
        StorageImplementation


class TestCommentRepliesCount:

    @pytest.mark.django_db
    def test_with_commments_having_replies(self,
                                           create_comments,
                                           create_replies):

        # Arrange
        comment_ids = [1, 2, 3, 4]
        sql_storage = StorageImplementation()
        expected_response = []

        # Act
        response = sql_storage.get_comment_replies_count(comment_ids=comment_ids)

        # Assert
        assert response == expected_response


    # @pytest.mark.django_db
    # def test_with_valid_domain_id_does_not_raises_exception(self, create_domains):
    #
    #     # Arrange
    #     domain_id = 1
    #     sql_storage = StorageImplementation()
    #
    #     # Act
    #     sql_storage.validate_domain_id(domain_id=domain_id)
