from django.db import models

from cms.models.pluginmodel import CMSPlugin
from django.db.models import ImageField, FileField


class HeadlinePluginModel(CMSPlugin):
    text = models.CharField(max_length=128)
    link = models.CharField(max_length=128)

    def __str__(self):
        return self.text

class ParallaxPluginModel(CMSPlugin):
    bild = ImageField(upload_to='parallax-background-images/')
    text = models.CharField(max_length=128, blank=True)

    def __str__(self):
        return self.text

class SplitParagraphPluginModel(CMSPlugin):
    text = models.TextField()

    def __str__(self):
        return self.text

class MapPluginModel(CMSPlugin):
    karte_1_bild = FileField(upload_to='map-images/')
    legende_1_bild = FileField(upload_to='map-images/')
    legende_1_text = models.CharField(max_length=128)

    karte_2_bild = FileField(upload_to='map-images/')
    legende_2_bild = FileField(upload_to='map-images/')
    legende_2_text = models.CharField(max_length=128)

    karte_3_bild = FileField(upload_to='map-images/')
    legende_3_bild = FileField(upload_to='map-images/')
    legende_3_text = models.CharField(max_length=128)

class ListAndImagePluginModel(CMSPlugin):
    ueberschrift = models.CharField(max_length=128)
    bild = FileField(upload_to='list-images/')
    stichkpunkt_1 = models.CharField(max_length=1024, blank=True)
    stichkpunkt_2 = models.CharField(max_length=1024, blank=True)
    stichkpunkt_3 = models.CharField(max_length=1024, blank=True)
    stichkpunkt_4 = models.CharField(max_length=1024, blank=True)
    stichkpunkt_5 = models.CharField(max_length=1024, blank=True)
    stichkpunkt_6 = models.CharField(max_length=1024, blank=True)
    stichkpunkt_7 = models.CharField(max_length=1024, blank=True)
    stichkpunkt_8 = models.CharField(max_length=1024, blank=True)
    stichkpunkt_9 = models.CharField(max_length=1024, blank=True)
    stichkpunkt_10 = models.CharField(max_length=1024, blank=True)

    def __str__(self):
        return self.ueberschrift
