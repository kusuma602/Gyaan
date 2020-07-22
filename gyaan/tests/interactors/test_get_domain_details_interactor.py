from unittest.mock import create_autospec, Mock


import pytest


from gyaan.interactors.get_domain_details_interactor import \
    GetDomainDetailsInteractor

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

    def test_with_invalid_domain_id_raises_exception(self,
                                                     storage_mock,
                                                     presenter_mock):
        from gyaan.exceptions.custom_exceptions import InvalidDomainID

        # Arrange
        domain_id = 1
        expected_response = Mock()
        interactor = GetDomainDetailsInteractor(
            storage=storage_mock
        )
        storage_mock.validate_domain_id.side_effect = InvalidDomainID
        presenter_mock.raise_invalid_domain_id_exception.return_value = \
            expected_response

        # Act
        response = interactor.get_domain_details_wrapper(
            presenter=presenter_mock, domain_id=domain_id
        )

        # Assert
        assert response == expected_response

    def test_with_valid_domain_id_returns_complete_domain_dto(self,
                                                              storage_mock,
                                                              presenter_mock,
                                                              domain_dto):

        # Arrange
        domain_id = 1
        expected_response = Mock()
        interactor = GetDomainDetailsInteractor(
            storage=storage_mock
        )
        storage_mock.get_domain_dto.return_value = domain_dto

        # Act
        response = interactor.get_domain_details_wrapper(
            presenter=presenter_mock, domain_id=domain_id
        )

        # Assert
        assert response == expected_response


