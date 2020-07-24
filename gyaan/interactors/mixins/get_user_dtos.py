from typing import List


from gyaan.adapters.service_adapter import ServiceAdapter


class GetUserDtosMixin:

    def get_user_dtos(self, user_ids: List[int]):
        service_adapter = ServiceAdapter()
        user_dtos = service_adapter.auth_service.get_user_dtos(
            user_ids=user_ids
        )
        return user_dtos
