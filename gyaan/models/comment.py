from django.db import models

from gyaan.models import Post


class Comment(models.Model):
    commented_by_id = models.IntegerField()
    commented_at = models.DateTimeField(auto_now=True)
    comment_content = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    approved_by_id = models.IntegerField(null=True)
