import factory
from datetime import datetime

from gyaan.constants.enums import ReactionChoices
from gyaan.models import Domain, DomainFollower, Post, DomainExpert
from gyaan.models.comment import Comment
from gyaan.models.reaction import Reaction


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


class CommentFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Comment

    comment_content = factory.Sequence(lambda n: "comment_{0}_content".format(n+1))
    commented_by_id = factory.Sequence(lambda n: n+1)
    post = factory.SubFactory(PostFactory)
    commented_at = factory.LazyFunction(datetime.now)


class ReplyFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Comment

    comment_content = factory.Sequence(lambda n: "comment_{0}_content".format(n+1))
    commented_by_id = factory.Sequence(lambda n: n+1)
    parent_comment = factory.Iterator(Comment.objects.all())
    commented_at = factory.LazyFunction(datetime.now)


REACTION_CHOICES = ReactionChoices.get_list_of_values()


class PostReactionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Reaction

    reaction = factory.Iterator(REACTION_CHOICES)
    reacted_by_id = factory.Sequence(lambda n: n+1)
    post = factory.SubFactory(PostFactory)
    comment = factory.SubFactory(CommentFactory)


class CommentReactionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Reaction

    reaction = factory.Iterator(REACTION_CHOICES)
    reacted_by_id = factory.Sequence(lambda n: n+1)
    comment = factory.SubFactory(CommentFactory)
