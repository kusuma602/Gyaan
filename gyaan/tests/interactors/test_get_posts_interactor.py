from unittest.mock import create_autospec, Mock

import pytest

from gyaan.interactors.get_posts_interactor import GetPostsInteractor
from gyaan.tests.common_fixtures.adapters.auth_service import prepare_get_user_dtos_mock


class TestGetPostsInteractor:
    @pytest.fixture
    def storage_mock(self):
        from gyaan.interactors.storages.storage_interface \
            import StorageInterface
        storage_mock = create_autospec(StorageInterface)
        return storage_mock

    @pytest.fixture
    def presenter_mock(self):
        from gyaan.interactors.presenters.presenter_interface \
            import GetPostsPresenterInterface
        presenter_mock = create_autospec(GetPostsPresenterInterface)
        return presenter_mock

    def test_with_invalid_post_ids_raises_exception(self,
                                                    presenter_mock,
                                                    storage_mock,
                                                    mocker):
        # Arrange
        interactor = GetPostsInteractor(storage=storage_mock)
        post_ids = [1, 2]
        expected_response = Mock()
        storage_mock.get_valid_post_ids.return_value = [1]
        presenter_mock.return_invalid_posts_response.return_value = \
            expected_response

        # Act
        response = interactor.get_posts_wrapper(
            presenter=presenter_mock,
            post_ids=post_ids
        )

        # Assert
        assert response == expected_response
        storage_mock.get_valid_post_ids.assert_called_once_with(
            post_ids=post_ids
        )
        presenter_mock.return_invalid_posts_response.assert_called_once()

    def test_with_valid_post_ids_returns_post_dtos(self,
                                                   mocker,
                                                   presenter_mock,
                                                   storage_mock,
                                                   post_dtos,
                                                   post_reactions_count_dto,
                                                   post_comments_count_dto,
                                                   comment_reactions_count_dto,
                                                   comment_dtos):
        # Arrange
        interactor = GetPostsInteractor(storage=storage_mock)
        post_ids = [1, 2]
        user_ids = [1, 2, 3, 4, 5]
        latest_comment_ids = [1, 2]
        expected_response = Mock()
        storage_mock.get_valid_post_ids.return_value = [1, 2]
        storage_mock.get_post_dtos.return_value = post_dtos
        storage_mock.get_post_reactions_counts.return_value = \
            post_reactions_count_dto
        storage_mock.get_post_comments_count.return_value = \
            post_comments_count_dto
        storage_mock.get_latest_comment_ids.return_value = latest_comment_ids
        storage_mock.get_comment_dtos.return_value = comment_dtos
        storage_mock.get_comment_reactions_count.return_value = \
            comment_reactions_count_dto
        get_user_dtos_mocker = prepare_get_user_dtos_mock(
            mocker, user_ids=user_ids
        )
        user_dto = get_user_dtos_mocker.return_value
        presenter_mock.get_posts_response.return_value = expected_response

        # Act
        response = interactor.get_posts_wrapper(
            presenter=presenter_mock,
            post_ids=post_ids
        )

        # Assert
        assert response == expected_response
        storage_mock.get_valid_post_ids.assert_called_once_with(
            post_ids=post_ids
        )
        storage_mock.get_post_dtos.assert_called_once_with(post_ids)
        storage_mock.get_post_reactions_counts.assert_called_once_with(
            post_ids
        )
        storage_mock.get_post_comments_count.assert_called_once_with(
            latest_comment_ids
        )
        #storage_mock.get_latest_comment_ids.calls_count()
        storage_mock.get_comment_dtos.assert_called_once_with(
            latest_comment_ids
        )
        storage_mock.get_comment_reactions_count.assert_called_once_with(
            latest_comment_ids
        )
