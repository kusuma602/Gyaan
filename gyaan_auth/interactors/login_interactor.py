from common.oauth_user_auth_tokens_service import OAuthUserAuthTokensService
from gyaan_auth.exceptions import InvalidUsername, InvalidPassword
from gyaan_auth.interactors.presenter_interfaces.presenter_interface import \
    LoginPresenterInterface
from gyaan_auth.interactors.storage_interfaces.storage_interface import \
    StorageInterface
from common.oauth2_storage import OAuth2SQLStorage


class LoginInteractor:

    def __init__(self, storage: StorageInterface, oauth2_storage: OAuth2SQLStorage):
        self.storage = storage
        self.oauth2_storage = oauth2_storage

    def login_wrapper(self,
                      presenter: LoginPresenterInterface,
                      username: str,
                      password: str):

        try:
            return self.login_response(presenter=presenter,
                                       username=username,
                                       password=password)
        except InvalidUsername:
            response = presenter.raise_invalid_username_exception()
        except InvalidPassword:
            response = presenter.raise_invalid_password_exception()

        return response

    def login_response(self,
                       presenter: LoginPresenterInterface,
                       username: str,
                       password: str):

        user_with_tokens_dto = self.login(
            username=username, password=password
        )
        response = presenter.get_login_response(
            user_with_tokens_dto=user_with_tokens_dto
        )
        return response

    def login(self, username, password):
        from gyaan_auth.interactors.dtos import UserWithTokensDTO
        self.storage.validate_username(username=username)
        user_id = self.storage.validate_password(
            username=username, password=password
        )

        user_dto = self.storage.get_user_dto(user_id=user_id)

        oauth = OAuthUserAuthTokensService(oauth2_storage=self.oauth2_storage)
        user_tokens_dto = oauth.create_user_auth_tokens(user_id=user_id)

        user_with_tokens_dto = UserWithTokensDTO(
            user_dto=user_dto, auth_token_dto=user_tokens_dto
        )
        return user_with_tokens_dto
