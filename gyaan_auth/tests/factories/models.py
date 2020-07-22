import factory


from gyaan_auth.models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    #UserFactory.reset_sequence(1)
    username = factory.Sequence(lambda n: "username_{0}".format(n+1))
    name = factory.Sequence(lambda n: "user_{0}".format(n + 1))
    profile_pic = factory.Sequence(lambda n: "profile_pic_{0}".format(n+1))
    is_admin = False
    is_domain_expert = False
