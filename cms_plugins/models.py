from django.db import models

from cms.models.pluginmodel import CMSPlugin
from django.db.models import ImageField, FileField


class HeadlinePluginModel(CMSPlugin):
    text = models.CharField(max_length=128)

class ParallaxPluginModel(CMSPlugin):
    bild = ImageField(upload_to='parallax-background-images/')
    text = models.CharField(max_length=128, blank=True)

class SplitParagraphPluginModel(CMSPlugin):
    text = models.TextField()

class MapPluginModel(CMSPlugin):
    karte_bild = FileField(upload_to='map-images/')
    legende_1_bild = FileField(upload_to='map-images/') 
    legende_1_text = models.CharField(max_length=128)
    legende_2_bild = FileField(upload_to='map-images/') 
    legende_2_text = models.CharField(max_length=128)
    legende_3_bild = FileField(upload_to='map-images/') 
    legende_3_text = models.CharField(max_length=128)