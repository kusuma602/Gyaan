
from django.db import models


from gyaan.constants.enums import RequestStatus
from gyaan.models import Domain


request_choices = RequestStatus.get_list_of_tuples()


class JoinRequest(models.Model):
    requested_by_id = models.IntegerField()
    approved_by_id = models.IntegerField(null=True)
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE)
    status = models.CharField(choices=request_choices, max_length=20)
