from django.db import models


from gyaan.models import Domain, Tag


class Post(models.Model):
    title = models.TextField()
    description = models.TextField()
    posted_at = models.DateTimeField(auto_now=True)
    posted_by_id = models.IntegerField()
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE)
    approved_by_id = models.IntegerField(null=True)
    tag = models.ManyToManyField(Tag)
