# pylint: disable=wrong-import-position

APP_NAME = "gyaan_auth"
OPERATION_NAME = "signin_user"
REQUEST_METHOD = "post"
URL_SUFFIX = "user/login/v1/"

from .test_case_01 import TestCase01SigninUserAPITestCase

__all__ = [
    "TestCase01SigninUserAPITestCase"
]
