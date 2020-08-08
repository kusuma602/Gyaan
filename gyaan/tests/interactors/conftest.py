import pytest


from gyaan.tests.factories.storage_dtos import (
    DomainDTOFactory,
    PostDTOFactory,
    PostCommentsCountDTOFactory,
    PostReactionsCountDTOFactory,
    CommentReactionsCountDTOFactory, CommentDTOFactory
)


@pytest.fixture
def domain_dto():
    domain_dto_factory = DomainDTOFactory()
    return domain_dto_factory


@pytest.fixture
def post_dtos():
    post_dto_factories = PostDTOFactory.create_batch(5)
    return post_dto_factories


@pytest.fixture
def post_comments_count_dto():
    comments_count = PostCommentsCountDTOFactory()
    return comments_count


@pytest.fixture
def post_reactions_count_dto():
    post_reaction_factories = PostReactionsCountDTOFactory()
    return post_reaction_factories


@pytest.fixture
def comment_reactions_count_dto():
    post_reaction_factories = CommentReactionsCountDTOFactory()
    return post_reaction_factories


@pytest.fixture()
def comment_dtos():
    comment_dtos = CommentDTOFactory.create_batch(4)
    return comment_dtos
