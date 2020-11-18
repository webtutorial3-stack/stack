from django.contrib.sitemaps import Sitemap

from django.shortcuts import reverse



#class CategorySitemap(Sitemap):
#    changefreq = "daily"
#    priority = 0.8
#    protocol = "https"
#
#    def items(self):
#        return Category.objects.all()
#
#
class StaticViewSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8
    protocol = "https"

    def items(self):
        return item.objects.all()


class StaticViewSitemap(Sitemap):
    protocol = "https"
    
    def items(self):
        return [
            'home',
            'aboutus',
            'shop',
            'faq',
            'pay',
        ]

    def location(self, item):
        return reverse(item)






