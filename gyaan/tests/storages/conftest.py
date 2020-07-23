import pytest


@pytest.fixture
@pytest.mark.django_db
def create_domains():
    from gyaan.tests.factories.models import DomainFactory
    domain_factories = DomainFactory.create_batch(7)
    return domain_factories


@pytest.fixture
@pytest.mark.django_db
def create_domain_posts():
    from gyaan.tests.factories.models import PostFactory
    domain_posts = PostFactory.create_batch(4)
    return domain_posts


@pytest.fixture
@pytest.mark.django_db
def create_domain_members():
    from gyaan.tests.factories.models import DomainFollowerFactory
    domain_followers_dto = DomainFollowerFactory.create_batch(3, domain_id=1)
    return domain_followers_dto


@pytest.fixture
@pytest.mark.django_db
def create_domain_experts():
    from gyaan.tests.factories.models import DomainExpertFactory
    DomainExpertFactory.reset_sequence()
    domain_experts_dto = DomainExpertFactory.create_batch(3, domain_id=1)
    return domain_experts_dto

