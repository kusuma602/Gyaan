from unittest.mock import create_autospec

import pytest


from gyaan.interactors.get_domain_details_interactor import \
    GetDomainDetailsInteractor
from gyaan.tests.common_fixtures.adapters.auth_service import \
    prepare_get_user_dtos_mock


class TestGetDomainDetails:

    @pytest.fixture
    def storage_mock(self):
        from gyaan.interactors.storages.storage_interface import \
            StorageInterface
        storage_mock = create_autospec(StorageInterface)
        return storage_mock

    @pytest.fixture
    def presenter_mock(self):
        from gyaan.interactors.presenters.presenter_interface import \
            GetDomainDetailsPresenterInterface
        presenter_mock = create_autospec(GetDomainDetailsPresenterInterface)
        return presenter_mock
