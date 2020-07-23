import factory


from gyaan.storages.dtos import DomainDTO


class DomainDTOFactory(factory.Factory):
    class Meta:
        model = DomainDTO

    domain_id = factory.sequence(lambda n: n + 1)
    domain_name = factory.Sequence(lambda n: "domain_{0}".format(n + 1))
    description = factory.sequence(lambda n: "domain_{0} description".format(n + 1))
