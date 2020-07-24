# pylint: disable=wrong-import-position

APP_NAME = "gyaan_auth"
OPERATION_NAME = "signin_user"
REQUEST_METHOD = "post"
URL_SUFFIX = "user/login/v1/"


from .test_case_01 import TestCase01SigninUserAPITestCase
from .test_case_02 import TestCase02SigninUserAPITestCase
from .test_case_03 import TestCase03SigninUserAPITestCase
from .test_case_04 import TestCase04SigninUserAPITestCase
from .test_case_05 import TestCase05SigninUserAPITestCase

__all__ = [
    "TestCase01SigninUserAPITestCase",
    "TestCase02SigninUserAPITestCase",
    "TestCase03SigninUserAPITestCase",
    "TestCase04SigninUserAPITestCase",
    "TestCase05SigninUserAPITestCase"
]

