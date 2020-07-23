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
                                                     storage_mock):
        from gyaan.exceptions.custom_exceptions import InvalidDomainID

        # Arrange
        domain_id = 1
        interactor = GetDomainDetailsInteractor(
            storage=storage_mock
        )
        storage_mock.validate_domain_id.side_effect = InvalidDomainID

        # Act
        with pytest.raises(InvalidDomainID):
            interactor.get_domain_details(domain_id=domain_id)

    def test_with_valid_domain_id_returns_complete_domain_dto(self,
                                                              storage_mock,
                                                              domain_dto,
                                                              mocker):
        from gyaan.adapters.dtos import UserDTO
        from gyaan.interactors.dtos import CompleteDomainDetailsDTO
        from gyaan.storages.dtos import DomainDTO
        # Arrange
        domain_id = 1
        expected_response = Mock()
        interactor = GetDomainDetailsInteractor(
            storage=storage_mock
        )
        expert_ids = [1, 2]
        expected_response = CompleteDomainDetailsDTO(
            domain_dto=DomainDTO(
                domain_id=1,
                domain_name='domain_1',
                description='domain_1 description'
            ),
            domain_posts_count=2,
            domain_members_count=3,
            book_marks_count=4,
            domain_expert_dtos=[
                UserDTO(
                    user_id=1,
                    name='user_1',
                    is_admin=False,
                    is_domain_expert=False
                ),
                UserDTO(
                    user_id=2,
                    name='user_2',
                    is_admin=False,
                    is_domain_expert=False
                )
            ]
        )
        posts_count = 2
        members_count = 3
        book_marks_count = 4
        storage_mock.get_domain_dto.return_value = domain_dto
        storage_mock.get_domain_posts_count.return_value = posts_count
        storage_mock.get_domain_members_count.return_value = members_count
        storage_mock.get_domain_book_marks_count.return_value = book_marks_count
        storage_mock.get_domain_experts_ids.return_value = expert_ids
        get_user_dtos_mocker = prepare_get_user_dtos_mock(
            mocker, user_ids=expert_ids
        )
        user_dto = get_user_dtos_mocker.return_value

        # Act
        response = interactor.get_domain_details(
            domain_id=domain_id
        )

        # Assert
        assert response == expected_response
