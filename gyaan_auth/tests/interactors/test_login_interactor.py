import pytest

from unittest.mock import create_autospec, patch, Mock

from gyaan_auth.interactors.login_interactor import LoginInteractor
from gyaan_auth.exceptions import InvalidPassword, InvalidUsername
from common.oauth_user_auth_tokens_service import OAuthUserAuthTokensService


class TestLoginInteractor:

    @pytest.fixture
    def storage_mock(self):
        from gyaan_auth.interactors.storage_interfaces.storage_interface \
            import StorageInterface
        storage_mock = create_autospec(StorageInterface)
        return storage_mock

    @pytest.fixture
    def presenter_mock(self):
        from gyaan_auth.interactors.presenter_interfaces.presenter_interface \
            import LoginPresenterInterface
        presenter_mock = create_autospec(LoginPresenterInterface)
        return presenter_mock

    @pytest.fixture
    def oauth_storage_mock(self):
        from common.oauth2_storage import OAuth2SQLStorage
        oauth_storage_mock = create_autospec(OAuth2SQLStorage)
        return oauth_storage_mock

    def test_with_valid_invalid_username_raises_exception(self,
                                                          storage_mock,
                                                          presenter_mock,
                                                          oauth_storage_mock):
        # Arrange
        username = "username"
        password = "password"
        expected_response = Mock()
        login_interactor = LoginInteractor(
            storage=storage_mock, oauth2_storage=oauth_storage_mock
        )
        storage_mock.validate_username.side_effect = InvalidUsername
        presenter_mock.raise_invalid_username_exception.return_value = \
            expected_response

        # Act
        response = login_interactor.login_wrapper(presenter=presenter_mock,
                                                  username=username,
                                                  password=password)

        # Assert
        assert response == expected_response
        storage_mock.validate_username.assert_called_once_with(username)
        presenter_mock.raise_invalid_username_exception.assert_called_once()

    def test_with_valid_invalid_password_raises_exception(self,
                                                          storage_mock,
                                                          presenter_mock,
                                                          oauth_storage_mock):
        # Arrange
        username = "username"
        password = "password"
        expected_response = Mock()
        login_interactor = LoginInteractor(
            storage=storage_mock, oauth2_storage=oauth_storage_mock
        )
        storage_mock.validate_password.side_effect = InvalidPassword
        presenter_mock.raise_invalid_password_exception.return_value = \
            expected_response

        # Act
        response = login_interactor.login_wrapper(presenter=presenter_mock,
                                                  username=username,
                                                  password=password)

        # Assert
        assert response == expected_response
        storage_mock.validate_password.assert_called_once_with(
            username, password
        )
        presenter_mock.raise_invalid_password_exception.assert_called_once()

    @patch.object(OAuthUserAuthTokensService, 'create_user_auth_tokens')
    def test_with_valid_details_returns_access_token(self,
                                                     storage_mock,
                                                     presenter_mock,
                                                     oauth_storage_mock,
                                                     user_token_dto,
                                                     user_dto):
        # Arrange
        from gyaan_auth.interactors.dtos import UserWithTokensDTO
        username = "username"
        password = "password"
        user_id = 1
        expected_response = Mock()
        login_interactor = LoginInteractor(
            storage=storage_mock, oauth2_storage=oauth_storage_mock)
        OAuthUserAuthTokensService.create_user_auth_tokens.return_value = \
            user_token_dto
        storage_mock.validate_password.return_value = user_id
        storage_mock.get_user_dto.return_value = user_dto
        presenter_mock.get_login_response.return_value = expected_response
        user_with_tokens_dto = UserWithTokensDTO(
            user_dto=user_dto,
            auth_token_dto=user_token_dto
        )

        # Act
        response = login_interactor.login_wrapper(presenter=presenter_mock,
                                                  username=username,
                                                  password=password)

        # Assert
        assert response == expected_response
        storage_mock.get_user_dto.assert_called_once_with(user_id=user_id)
        presenter_mock.get_login_response.assert_called_once_with(user_with_tokens_dto)
