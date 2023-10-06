from django.db import models

class Bundle(models.Model):
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255, blank=True, null=True)

class Link(models.Model):
    bundle = models.ForeignKey(Bundle, on_delete=models.CASCADE)
    url = models.URLField()
