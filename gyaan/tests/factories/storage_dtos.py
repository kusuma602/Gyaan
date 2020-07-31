import factory
from datetime import datetime


from gyaan.storages.dtos import (
    DomainDTO, PostDTO, PostCommentsCountDTO, PostReactionsCountDTO, CommentReactionsCountDTO, CommentDTO,
    CommentRepliesCountDTO
)


class DomainDTOFactory(factory.Factory):
    class Meta:
        model = DomainDTO

    domain_id = factory.sequence(lambda n: n + 1)
    domain_name = factory.Sequence(lambda n: "domain_{0}".format(n + 1))
    description = factory.sequence(lambda n: "domain_{0} description".format(n + 1))


class PostDTOFactory(factory.Factory):
    class Meta:
        model = PostDTO

    post_id = factory.sequence(lambda n: n + 1)
    title = factory.Sequence(lambda n: "post_title_{0}".format(n + 1))
    description = factory.sequence(lambda n: "post_{0} description".format(n + 1))
    posted_at = factory.LazyFunction(datetime.now)
    posted_by_id = factory.sequence(lambda n: n + 1)
    domain_id = factory.sequence(lambda n: n + 1)


class PostCommentsCountDTOFactory(factory.Factory):
    class Meta:
        model = PostCommentsCountDTO

    post_id = factory.sequence(lambda n: n + 1)
    comments_count = factory.sequence(lambda n: n + 1)


class PostReactionsCountDTOFactory(factory.Factory):
    class Meta:
        model = PostReactionsCountDTO

    post_id = factory.sequence(lambda n: n + 1)
    reactions_count = factory.sequence(lambda n: n + 1)


class CommentRepliesCountDTOFactory(factory.Factory):
    class Meta:
        model = CommentRepliesCountDTO

    comment_id = factory.sequence(lambda n: n + 1)
    replies_count = factory.sequence(lambda n: n + 1)


class CommentReactionsCountDTOFactory(factory.Factory):
    class Meta:
        model = CommentReactionsCountDTO

    comment_id = factory.sequence(lambda n: n + 1)
    reactions_count = factory.sequence(lambda n: n + 1)


class CommentDTOFactory(factory.Factory):
    class Meta:
        model = CommentDTO

    comment_id = factory.sequence(lambda n: n + 1)
    comment_content = factory.sequence(lambda n: "comment_{0}_content".format(n + 1))
    commented_at = factory.LazyFunction(datetime.now)
    commented_by_id = factory.sequence(lambda n: n + 1)
    post_id = factory.sequence(lambda n: n + 1)
