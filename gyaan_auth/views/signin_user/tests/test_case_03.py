"""
# TODO: Test Login Valid User Valid Details Returns Access_Token
"""
from unittest.mock import patch

from django_swagger_utils.utils.test import CustomAPITestCase

from common.dtos import UserAuthTokensDTO
from common.oauth_user_auth_tokens_service import OAuthUserAuthTokensService
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from gyaan_auth.utils.custom_test_utils import CustomTestUtils

REQUEST_BODY = """
{
    "username": "username",
    "password": "password"
}
"""

TEST_CASE = {
    "request": {
        "path_params": {},
        "query_params": {},
        "header_params": {},
        "securities": {},
        "body": REQUEST_BODY,
    },
}


class TestCase03SigninUserAPITestCase(CustomTestUtils):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE

    @patch.object(OAuthUserAuthTokensService, 'create_user_auth_tokens')
    def test_case(self, user_token_dto):
        import json
        self.create_user()
        user_token_dto = UserAuthTokensDTO(
            user_id=1,
            access_token="user access token",
            refresh_token="user refresh token",
            expires_in=10000000
        )
        OAuthUserAuthTokensService.create_user_auth_tokens.return_value = \
            user_token_dto
        response = self.default_test_case()
        response_content = json.loads(response.content)
        self.assert_match_snapshot(
            name="token response",
            value=response_content
        )
