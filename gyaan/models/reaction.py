from django.db import models

from gyaan.constants.enums import ReactionChoices
from gyaan.models import Post
from gyaan.models.comment import Comment


class Reaction(models.Model):
    REACTION_CHOICES = ReactionChoices.get_list_of_tuples()
    reaction = models.CharField(choices=REACTION_CHOICES, max_length=20)
    reacted_by_id = models.IntegerField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True)
