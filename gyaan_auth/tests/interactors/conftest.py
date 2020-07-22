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
def user_with_tokens_dto():
    from gyaan_auth.interactors.dtos import UserWithTokensDTO
    user_with_tokens_dto = UserWithTokensDTO(
        user_dto=user_dto,
        auth_token_dto=user_token_dto
    )
    return user_with_tokens_dto
