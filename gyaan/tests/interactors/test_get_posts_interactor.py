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
            import GetPostsPeresenterInterface
        presenter_mock = create_autospec(GetPostsPeresenterInterface)
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
        presenter_mock.return_invalid_posts_response.called_once()

    def test_with_valid_post_ids_returns_post_dtos(self,
                                                   presenter_mock,
                                                   storage_mock):
        pass
