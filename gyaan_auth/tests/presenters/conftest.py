import pytest
import datetime


@pytest.fixture()
def user_token_dto():
    from common.dtos import UserAuthTokensDTO
    user_access_token = UserAuthTokensDTO(
        access_token="user_access_token",
        refresh_token="user_refresh_token",
        expires_in=datetime.datetime(2020, 5, 27, 11, 13, 44, 954147),
        user_id=1
    )
    return user_access_token


@pytest.fixture()
def user_dto():
    from gyaan_auth.tests.factories.storage_dtos import UserDTOFactory
    user_dto = UserDTOFactory()
    return user_dto


@pytest.fixture()
def login_response():
    response = {
        "access_token": "user_access_token",
        "is_admin": False,
        "is_domain_expert": False
    }
    return response
