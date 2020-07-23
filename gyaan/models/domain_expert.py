from django.db import models


from gyaan.models import Domain


class DomainExpert(models.Model):
    expert_id = models.IntegerField()
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE)