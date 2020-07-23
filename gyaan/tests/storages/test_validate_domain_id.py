import pytest


from gyaan.storages.storage_implementation import \
        StorageImplementation


class TestValidateDomainID:

    @pytest.mark.django_db
    def test_with_invalid_domain_id_raises_exception(self, create_domains):
        from gyaan.exceptions.custom_exceptions import InvalidDomainID

        # Arrange
        domain_id = 10
        sql_storage = StorageImplementation()

        # Act
        with pytest.raises(InvalidDomainID):
            sql_storage.validate_domain_id(domain_id=domain_id)

    @pytest.mark.django_db
    def test_with_valid_domain_id_does_not_raises_exception(self, create_domains):

        # Arrange
        domain_id = 1
        sql_storage = StorageImplementation()

        # Act
        sql_storage.validate_domain_id(domain_id=domain_id)
