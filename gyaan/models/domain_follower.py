from django.db import models

from gyaan.models import Domain


class DomainFollower(models.Model):
    follower_id = models.IntegerField()
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE)
