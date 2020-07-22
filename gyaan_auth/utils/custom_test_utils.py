from django_swagger_utils.utils.test import CustomAPITestCase
from django.contrib.auth.hashers import make_password


class CustomTestUtils(CustomAPITestCase):

    def create_user(self):
        from gyaan_auth.tests.factories.models import UserFactory
        UserFactory.reset_sequence(1)
        UserFactory.create(
            username="username", password=make_password("password")
        )
    def create_admin(self):
        from gyaan_auth.tests.factories.models import UserFactory
        UserFactory.reset_sequence(1)
        UserFactory.create(
            username="admin",
            password=make_password("password"),
            is_admin=True
        )

    def create_domain_expert(self):
        from gyaan_auth.tests.factories.models import UserFactory
        UserFactory.reset_sequence(1)
        UserFactory.create(
            username="domain_expert",
            password=make_password("password"),
            is_domain_expert=True
        )