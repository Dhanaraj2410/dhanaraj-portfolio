"""
Django sitemaps for SEO (static, no database).
"""
from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from . import content


class StaticViewSitemap(Sitemap):
    priority = 1.0
    changefreq = 'weekly'

    def items(self):
        return ['core:home']

    def location(self, item):
        return reverse(item)


class ProjectSitemap(Sitemap):
    priority = 0.8
    changefreq = 'monthly'

    def items(self):
        return content.PROJECTS

    def location(self, obj):
        return reverse('core:project_detail', kwargs={'slug': obj.slug})