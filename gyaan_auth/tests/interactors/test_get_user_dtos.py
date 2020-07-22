import pytest

from unittest.mock import create_autospec, Mock

from gyaan_auth.interactors.get_user_dtos import GetUserDtosInteractor


class TestGetUserDtos:

    @pytest.fixture
    def storage_mock(self):
        from gyaan_auth.interactors.storage_interfaces.storage_interface \
            import StorageInterface
        storage_mock = create_autospec(StorageInterface)
        return storage_mock

    @pytest.fixture
    def presenter_mock(self):
        from gyaan_auth.interactors.presenter_interfaces.presenter_interface \
            import GetUserDtoPresenterInterface
        presenter_mock = create_autospec(GetUserDtoPresenterInterface)
        return presenter_mock

    def test_with_invalid_user_ids_raises_exception(self,
                                                    storage_mock,
                                                    presenter_mock):

        # Arrange
        interactor = GetUserDtosInteractor(storage=storage_mock)
        user_ids = [1, 2, 3]
        invalid_ids = [3]
        expected_response = Mock()
        storage_mock.get_valid_user_ids.return_value = [1, 2]
        presenter_mock.raise_invalid_user_ids_exception.return_value = \
                expected_response

        # Act
        response = interactor.get_user_dtos_wrapper(
            presenter=presenter_mock,
            user_ids=user_ids)

        # Assert
        assert response == expected_response
        storage_mock.get_valid_user_ids.assert_called_once_with(user_ids)
        presenter_mock.raise_invalid_user_ids_exception.assert_called_once()
        # call_args = presenter_mock.raise_invalid_user_ids_exception.call_args
        # assert call_args.args[0].args[0] == invalid_ids

    def test_with_valid_user_ids_returns_user_dtos(self,
                                                   storage_mock,
                                                   presenter_mock,
                                                   user_dto):
        # Arrange
        interactor = GetUserDtosInteractor(storage=storage_mock)
        user_ids = [1, 2, 3]
        expected_response = [user_dto]
        storage_mock.get_valid_user_ids.return_value = [1, 2, 3]
        storage_mock.get_list_of_user_dtos.return_value = expected_response

        # Act
        repsonse = interactor.get_user_dtos_wrapper(
            presenter=presenter_mock,
            user_ids=user_ids
        )

        # Assert
        assert repsonse == expected_response
        storage_mock.get_list_of_user_dtos.assert_called_once_with(user_ids)
        storage_mock.get_valid_user_ids.assert_called_once_with(user_ids)