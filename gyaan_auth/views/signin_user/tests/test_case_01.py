"""
# TODO: Test Login User With Invalid Username raises Exception
"""

from django_swagger_utils.utils.test import CustomAPITestCase
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from gyaan_auth.utils.custom_test_utils import CustomTestUtils

REQUEST_BODY = """
{
    "username": "invalid username",
    "password": "invalid password"
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


class TestCase01SigninUserAPITestCase(CustomTestUtils):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE

    def test_case(self):
        import json
        self.create_user()
        response = self.default_test_case()
        response_content = json.loads(response.content)
        self.assert_match_snapshot(
            name="exception message",
            value=response_content['res_status']
        )