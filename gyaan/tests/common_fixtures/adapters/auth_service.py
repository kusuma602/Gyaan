from typing import List

from gyaan.adapters.dtos import UserDTO


def prepare_get_user_dtos_mock(mocker, user_ids: List[int]):
    mock = mocker.patch(
        'gyaan.adapters.auth_service.AuthService.get_user_dtos'
    )
    user_dtos = [
        UserDTO(
            user_id=user_id,
            name="user_{}".format(_index + 1),
            is_admin=False,
            is_domain_expert=False
        ) for _index, user_id in enumerate(user_ids)
    ]
    mock.return_value = user_dtos
    return mock

