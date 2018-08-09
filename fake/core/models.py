from django.db import models


class Fake(models.Model):
    url = models.URLField(max_length=300)
    counter = models.IntegerField(default=0)