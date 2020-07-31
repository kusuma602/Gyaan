from unittest.mock import create_autospec, Mock


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
        presenter_mock.get_invalid_domain_id_response.return_value = \
            expected_response

        # Act
        response = interactor.get_domain_details_wrapper(
            presenter=presenter_mock,
            domain_id=domain_id
        )

        # Assert
        assert response == expected_response
        storage_mock.validate_domain_id.assert_called_once_with(domain_id)
        presenter_mock.get_invalid_domain_id_response.assert_called_once()

    def test_with_valid_domain_id_returns_complete_domain_dto(self,
                                                              storage_mock,
                                                              domain_dto,
                                                              mocker,
                                                              presenter_mock):
        # Arrange
        domain_id = 1
        expected_response = Mock()
        interactor = GetDomainDetailsInteractor(
            storage=storage_mock
        )
        expert_ids = [1, 2]
        posts_count = 2
        members_count = 3
        book_marks_count = 4
        storage_mock.get_domain_dto.return_value = domain_dto
        storage_mock.get_domain_posts_count.return_value = posts_count
        storage_mock.get_domain_members_count.return_value = members_count
        storage_mock.get_domain_book_marks_count.return_value = \
            book_marks_count
        storage_mock.get_domain_experts_ids.return_value = expert_ids
        get_user_dtos_mocker = prepare_get_user_dtos_mock(
            mocker, user_ids=expert_ids
        )
        user_dto = get_user_dtos_mocker.return_value
        presenter_mock.get_domain_details_response.return_value = \
            expected_response

        # Act
        response = interactor.get_domain_details_wrapper(
            domain_id=domain_id,
            presenter=presenter_mock
        )

        # Assert
        assert response == expected_response
