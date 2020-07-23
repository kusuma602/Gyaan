import pytest


from gyaan.storages.storage_implementation import StorageImplementation


@pytest.mark.django_db
def test_get_domain_dto_with_domain_id_returns_domains_dto(create_domains):
    from gyaan.storages.dtos import DomainDTO
    # Arrange
    domain_id = 1
    sql_storage = StorageImplementation()
    expected_response = DomainDTO(
        domain_id=1,
        domain_name='domain_1',
        description='domain_1_description'
    )

    # Act
    domain_dto = sql_storage.get_domain_dto(domain_id=domain_id)

    # Assert
    assert domain_dto == expected_response
