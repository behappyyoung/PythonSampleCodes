from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from datetime import datetime


# class TrackerSitemap(Sitemap):
#     changefreq = "monthly"
#     priority = 0.9
#
#     def items(self):
#         return Users.objects.all()
#
#     def lastmod(self, obj):
#         try:
#             dt = datetime.strptime(obj.updated, '%Y-%m-%d %H:%M:%S')
#             return dt
#
#         except:
#             return datetime.today()
#
#     def location(self, item):
#         try:
#             if reverse(item):
#                 return reverse(item)
#             else:
#                 return [item]
#         except:
#             return ['--']


class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'never'

    def items(self):
        return ['index', 'user_profile']

    def location(self, item):
        return reverse(item)