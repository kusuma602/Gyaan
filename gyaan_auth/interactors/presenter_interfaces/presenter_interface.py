from abc import ABC
from abc import abstractmethod


from gyaan_auth.interactors.dtos import UserWithTokensDTO


class LoginPresenterInterface(ABC):

    @abstractmethod
    def raise_invalid_username_exception(self):
        pass

    @abstractmethod
    def raise_invalid_password_exception(self):
        pass

    @abstractmethod
    def get_login_response(self, user_with_tokens_dto: UserWithTokensDTO):
        pass


class GetUserDtoPresenterInterface(ABC):

    @abstractmethod
    def raise_invalid_user_ids_exception(self, err_object):
        pass
