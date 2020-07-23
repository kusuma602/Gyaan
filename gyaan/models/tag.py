from django.db import models


from gyaan.models import Domain


class Tag(models.Model):
    name = models.CharField(max_length=100)
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE)