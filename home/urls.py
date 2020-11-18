from django.contrib.sitemaps.views import sitemap
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from home import views
from .sitemaps import StaticViewSitemap

sitemaps = {

    'static': StaticViewSitemap,

}

urlpatterns = [
    path('', views.home, name="home"),
    path('index/', views.home, name="home"),
    path('order_confirmation/', views.order_confirmation, name="order_confirmation"),
    path('about/', views.aboutus, name='aboutus'),
    path('contact/', views.contactus, name='contact'),
    path('faq/', views.faq, name='faq'),
    path('pay/', views.pay, name='pay'),
    path('prodinfo/', views.prodinfo, name='prodinfo'),
    # path('gallery/', views.gallery, name='gallery'),
    # path('pricing/', views.pricing, name='pricing'),


    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),


    path('about/', views.aboutus, name='aboutus'),
    path('contact/', views.contactus, name='contact'),
    path('search/', views.search, name='search'),
    path('shop/', views.shop, name='shop'),
    path('category/', views.category, name='category'),
    path('search_auto/', views.search_auto, name='search_auto'),
    path('category/<int:id>/<slug:slug>', views.category_products, name='category_products'),
    path('product/<int:id>/<slug:slug>', views.product_detail, name='product_detail'),
#    path(r'^product/(?P<id>\d+)/(?P<slug>[-\w+])/$', views.product_detail, name='product_detail'),
    # path('ajaxtest/', views.ajaxtest, name='ajaxtest'),
    # path('ajaxpost/', views.ajaxpost, name='ajaxpost'),
    path('ajaxcolor/', views.ajaxcolor, name='ajaxcolor'),
    path('ajaxcolor/', views.ajaxcolor, name='ajaxcolor'),
]