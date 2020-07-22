import pytest

from gyaan.tests.factories.storage_dtos import DomainDTOFactory


@pytest.fixture
def domain_dto():
    domain_dto_factory = DomainDTOFactory()
    return domain_dto_factory
