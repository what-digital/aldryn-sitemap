from cms.sitemaps import CMSSitemap
from django.conf.urls import url

url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': {'cmspages': CMSSitemap}}),
