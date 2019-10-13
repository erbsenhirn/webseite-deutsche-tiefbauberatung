from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin

from .models import HeadlinePluginModel, ParallaxPluginModel, SplitParagraphPluginModel

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