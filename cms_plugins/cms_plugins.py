from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin

from .models import HeadlinePluginModel, ParallaxPluginModel, SplitParagraphPluginModel, MapPluginModel, ListAndImagePluginModel

@plugin_pool.register_plugin
class HeadLinePlugin(CMSPluginBase):
    name = 'Überschrift'
    model = HeadlinePluginModel
    render_template = "headline.html"

    def render(self, context, instance, placeholder):
        context = super(HeadLinePlugin, self).render(context, instance, placeholder)
        return context


@plugin_pool.register_plugin
class ParallaxPlugin(CMSPluginBase):
    name = 'Parallax Container'
    model = ParallaxPluginModel
    render_template = "parallax.html"

    def render(self, context, instance, placeholder):
        context = super(ParallaxPlugin, self).render(context, instance, placeholder)
        return context


@plugin_pool.register_plugin
class SplitParagraphPlugin(CMSPluginBase):
    name = 'Spaltentext'
    model = SplitParagraphPluginModel
    render_template = "split-paragraph.html"

    def render(self, context, instance, placeholder):
        context = super(SplitParagraphPlugin, self).render(context, instance, placeholder)
        return context
        
@plugin_pool.register_plugin
class MapPlugin(CMSPluginBase):
    name = 'Karte'
    model = MapPluginModel
    render_template = "map.html"

    def render(self, context, instance, placeholder):
        context = super(MapPlugin, self).render(context, instance, placeholder)
        return context
        
@plugin_pool.register_plugin
class ListAndImagePlugin(CMSPluginBase):
    name = 'List und Bild'
    model = ListAndImagePluginModel
    render_template = "list-and-image.html"

    def render(self, context, instance, placeholder):
        context = super(ListAndImagePlugin, self).render(context, instance, placeholder)
        return context