from django.db import models

class BaseDate(models.Model):
    date = models.DateTimeField()

    class Meta:
        abstract = True
