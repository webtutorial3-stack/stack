from django.urls import path
from home import views

urlpatterns = [
    path('', views.home, name="home"),
    path('home/', views.home, name="home"),
    path('about/', views.aboutus, name='aboutus'),
    path('contact/', views.contactus, name='contact'),
    path('faq/', views.faq, name='faq'),
    # path('gallery/', views.gallery, name='gallery'),
    # path('pricing/', views.pricing, name='pricing'),
    path('about/', views.aboutus, name='aboutus'),
    path('contact/', views.contactus, name='contact'),
    path('search/', views.search, name='search'),
    path('shop/', views.shop, name='shop'),
    path('category/', views.category, name='category'),
    path('search_auto/', views.search_auto, name='search_auto'),
    path('category/<int:id>/<slug:slug>', views.category_products, name='category_products'),
    path('product/<int:id>/<slug:slug>', views.product_detail, name='product_detail'),
    # path('ajaxtest/', views.ajaxtest, name='ajaxtest'),
    # path('ajaxpost/', views.ajaxpost, name='ajaxpost'),
    path('ajaxcolor/', views.ajaxcolor, name='ajaxcolor'),
    path('ajaxcolor/', views.ajaxcolor, name='ajaxcolor'),
]