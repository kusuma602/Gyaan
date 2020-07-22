import pytest
from django.contrib.auth.hashers import make_password

from gyaan_auth.tests.factories.models import UserFactory


@pytest.fixture
@pytest.mark.django_db
def create_users():
    UserFactory.reset_sequence()
    UserFactory.create_batch(5, password=make_password("password"))
