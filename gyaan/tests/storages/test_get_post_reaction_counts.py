import pytest


from gyaan.storages.storage_implementation import \
        StorageImplementation


class TestGetPostReactionCount:

    @pytest.mark.django_db
    def test_with_post_ids_returns_reaction_count_when_reaction_in_db(
            self,
            create_reactions_for_posts,
            create_post_reactions_count):

        # Arrange
        post_ids = [1, 2]
        sql_storage = StorageImplementation()
        expected_response = create_post_reactions_count

        # Act
        response = sql_storage.get_post_reactions_counts(post_ids=post_ids)

        # Assert
        assert response == expected_response

    @pytest.mark.django_db
    def test_with_post_ids_returns_reaction_count_when_no_reactions_in_db(
            self,
            create_post_reactions_count_when_no_reactions):

        # Arrange
        post_ids = [1, 2]
        sql_storage = StorageImplementation()
        expected_response = create_post_reactions_count_when_no_reactions

        # Act
        response = sql_storage.get_post_reactions_counts(post_ids=post_ids)

        # Assert
        assert response == expected_response
