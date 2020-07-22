# import pytest
#
#
# from unittest.mock import create_autospec
#
#
#
#
# class TestGetDomainDetails:
#     @pytest.fixture
#     def storage_mock(self):
#         from gyaan_auth.interactors.storage_interfaces.storage_interface \
#             import StorageInterface
#         storage_mock = create_autospec(StorageInterface)
#         return storage_mock
#
#     @pytest.fixture
#     def presenter_mock(self):
#         from gyaan_auth.interactors.presenter_interfaces.presenter_interface \
#             import LoginPresenterInterface
#         presenter_mock = create_autospec(LoginPresenterInterface)
#         return presenter_mock
#
#     def test_with_invalid_domain_id_raises_invalid_domain_id_exception(self):
#         # Arrange
#         interactor =
#
#         # Act
#
#         # Assert
