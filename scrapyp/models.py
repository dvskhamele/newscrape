from django.db import models

# Create your models here.
class Scrapy(models.Model):
    url_Links = models.CharField(blank=True, max_length=255)
    web_Links = models.CharField(blank=True, max_length=255)
    url_Image = models.CharField(blank=True, max_length=255)
    article_DownDate = models.CharField(blank=True, max_length=255)
    article_PubDownDate = models.CharField(blank=True, max_length=255)
    