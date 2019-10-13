from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin

from .models import HeadlinePluginModel, ParallaxPluginModel

@plugin_pool.register_plugin
class HeadLinePlugin(CMSPluginBase):
    name = 'Überschrift'
    model = HeadlinePluginModel
    render_template = "inline/headline.html"

    def render(self, context, instance, placeholder):
        context = super(HeadLinePlugin, self).render(context, instance, placeholder)
        return context


@plugin_pool.register_plugin
class ParallaxPlugin(CMSPluginBase):
    name = 'Parallax Container'
    model = ParallaxPluginModel
    render_template = "container/parallax.html"

    def render(self, context, instance, placeholder):
        context = super(ParallaxPlugin, self).render(context, instance, placeholder)
        return context