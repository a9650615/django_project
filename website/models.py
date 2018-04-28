from django.db import models

class CrawlData(models.Model):
    name = models.CharField(max_length=30)