from django.http import response


from gyaan_auth.interactors.dtos import UserWithTokensDTO
from gyaan_auth.interactors.presenter_interfaces.presenter_interface import \
    LoginPresenterInterface, GetUserDtoPresenterInterface


class LoginPresenterImplementation(LoginPresenterInterface):

    def raise_invalid_username_exception(self):
        import json
        from gyaan_auth.constants.exception_messages import INVALID_USERNAME
        data = json.dumps({
            "response": INVALID_USERNAME[0],
            "http_status_code": 404,
            "res_status": INVALID_USERNAME[1]
        })
        response_object = response.HttpResponse(data, status=404)
        return response_object

    def raise_invalid_password_exception(self):
        import json
        from gyaan_auth.constants.exception_messages import INVALID_PASSWORD
        data = json.dumps({
            "response": INVALID_PASSWORD[0],
            "http_status_code": 400,
            "res_status": INVALID_PASSWORD[1]
        })
        response_object = response.HttpResponse(data, status=400)
        return response_object

    def get_login_response(self, user_with_tokens_dto: UserWithTokensDTO):
        import json
        user_dto = user_with_tokens_dto.user_dto
        token_dto = user_with_tokens_dto.auth_token_dto
        data = json.dumps({
            "access_token": token_dto.access_token,
            "is_admin": user_dto.is_admin,
            "is_domain_expert": user_dto.is_domain_expert
        })
        response_object = response.HttpResponse(data, status=200)
        return response_object


class GetUserDtoPresenterImplementation(GetUserDtoPresenterInterface):

        def raise_invalid_user_ids_exception(self, err_object):
            import json
            from gyaan_auth.constants.exception_messages import INVALID_PASSWORD
            invalid_user_ids = err_object.invalid_user_ids

            invalid_ids_response = \
                f"{INVALID_PASSWORD[0]} Invalid user ids: {invalid_user_ids}"
            data = json.dumps({
                "response": invalid_ids_response,
                "http_status_code": 400,
                "res_status": INVALID_PASSWORD[1]
            })
            response_object = response.HttpResponse(data, status=400)
            return response_object
