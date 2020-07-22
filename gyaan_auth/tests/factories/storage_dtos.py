import factory
from gyaan_auth.storages.dtos import UserDTO


class UserDTOFactory(factory.Factory):
    class Meta:
        model = UserDTO

    user_id = factory.sequence(lambda n: n + 1)
    name = factory.Sequence(lambda n: "user_{0}".format(n + 1))
    is_admin = False
    is_domain_expert = False
