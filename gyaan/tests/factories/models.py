import factory
from datetime import datetime


from gyaan.models import Domain, DomainFollower, Post, DomainExpert


class DomainFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Domain

    name = factory.Sequence(lambda n: "domain_{0}".format(n+1))
    description = factory.Sequence(lambda n: "domain_{0}_description".format(n + 1))


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    title = factory.Sequence(lambda n: "post_title_{0}".format(n+1))
    description = factory.Sequence(lambda n: "post_{0}_description".format(n + 1))
    posted_at = factory.LazyFunction(datetime.now)
    domain = factory.SubFactory(DomainFactory)
    posted_by_id = factory.Sequence(lambda n: n+1)


class DomainFollowerFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = DomainFollower

    follower_id = factory.Sequence(lambda n: n+1)
    domain = factory.SubFactory(DomainFactory)


class DomainExpertFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = DomainExpert

    expert_id = factory.Sequence(lambda n: n+1)
    domain = factory.SubFactory(DomainFactory)
