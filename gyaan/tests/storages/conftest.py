import pytest
from freezegun import freeze_time


@pytest.fixture
@pytest.mark.django_db
def create_domains():
    from gyaan.tests.factories.models import DomainFactory
    DomainFactory.reset_sequence()
    domain_factories = DomainFactory.create_batch(7)
    return domain_factories


@pytest.fixture
@freeze_time("2020-07-31 00:00:00.000000")
def create_domain_posts():
    from gyaan.tests.factories.models import PostFactory
    PostFactory.reset_sequence()
    domain_posts = PostFactory.create_batch(4)
    return domain_posts


@pytest.fixture()
def create_reactions_for_posts():
    from gyaan.tests.factories.models import PostReactionFactory
    PostReactionFactory.reset_sequence()
    post_reactions = PostReactionFactory.create_batch(2)
    return post_reactions

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


@pytest.fixture()
@freeze_time("2020-07-31 00:00:00.000000")
def create_post_dto_factories():
    from gyaan.tests.factories.storage_dtos import PostDTOFactory
    PostDTOFactory.reset_sequence()
    post_dto_factories = PostDTOFactory.create_batch(4)
    return post_dto_factories


@pytest.fixture()
def create_post_reactions_count():
    from gyaan.tests.factories.storage_dtos import PostReactionsCountDTOFactory
    PostReactionsCountDTOFactory.reset_sequence()
    post_reaction_counts = PostReactionsCountDTOFactory.create_batch(2, reactions_count=1)
    return post_reaction_counts


@pytest.fixture()
def create_post_reactions_count_when_no_reactions():
    from gyaan.tests.factories.storage_dtos import PostReactionsCountDTOFactory
    PostReactionsCountDTOFactory.reset_sequence()
    post_reaction_counts = PostReactionsCountDTOFactory.create_batch(2, reactions_count=0)
    return post_reaction_counts


@pytest.fixture()
@freeze_time("2020-07-31 00:00:00.000000")
def create_comments():
    from gyaan.tests.factories.models import CommentFactory
    comment_dtos = CommentFactory.create_batch(4)
    return comment_dtos


@pytest.fixture()
@freeze_time("2020-07-31 00:00:00.000000")
def create_comment_dtos():
    from gyaan.tests.factories.storage_dtos import CommentDTOFactory
    comment_dto_factories = CommentDTOFactory.create_batch(4)
    return comment_dto_factories


@pytest.fixture()
def create_replies():
    from gyaan.tests.factories.models import ReplyFactory
    ReplyFactory.reset_sequence()
    replies = ReplyFactory.create_batch(4)
    return replies
