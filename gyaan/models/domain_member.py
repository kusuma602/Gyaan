from django.db import models


from gyaan.models import Domain


class DomainMember(models.Model):
    member_id = models.IntegerField()
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE)
    is_domain_expert = models.BooleanField(default=False)
