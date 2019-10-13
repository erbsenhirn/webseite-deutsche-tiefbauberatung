from django.db import models

from cms.models.pluginmodel import CMSPlugin
from django.db.models import ImageField


class HeadlinePluginModel(CMSPlugin):
    text = models.CharField(max_length=128)

class ParallaxPluginModel(CMSPlugin):
    bild = ImageField(upload_to='parallax-background-images/')
    text = models.CharField(max_length=128, blank=True)

class SplitParagraphPluginModel(CMSPlugin):
    text = models.TextField()