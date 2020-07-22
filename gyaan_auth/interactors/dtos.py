from gyaan_auth.storages.dtos import UserDTO
from common.dtos import UserAuthTokensDTO
from dataclasses import dataclass


@dataclass
class UserWithTokensDTO:
    user_dto: UserDTO
    auth_token_dto: UserAuthTokensDTO

