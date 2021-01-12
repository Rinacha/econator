from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.index, name='index'),
    path('explanation/', views.explain, name='explain'),
    path('search/', views.search, name='search'),
    #path(r'shop', views.index, name="index"),
    path('shop/', views.list_view, name="list_view"),
    path('shop/<int:pk>/', views.detail, name="detail"),
    #path('contact_form/', views.contact_form, name='contact_form'),
    #path('contact_form/complete/', views.complete, name='complete'),
    #path('tmp/', views.tmp, name='tmp'),

    # color
    path("search/color/",views.search_color, name='color'),
    path('color_black/', views.color_black, name='color_black'),
    path('color_blue/', views.color_blue, name='color_blue'),
    path('color_gray/', views.color_gray, name='color_gray'),
    path('color_green/', views.color_green, name='color_green'),
    path('color_red/', views.color_red, name='color_red'),
    path('color_white/', views.color_white, name='color_white'),
    path('color_yellow/', views.color_yellow, name='color_yellow'),

    # mate
    path("search/material/",views.search_mate, name='mate'),
    path('jusi/', views.jusi, name='jusi'),
    path('nylone/', views.nylone, name='nylone'),
    path('net/', views.net, name='net'),
    path('pori/', views.pori, name='pori'),
    path('unknown/', views.unknown, name='unknown'),

    # seller
    path("search/seller/",views.search_seller, name='seller'),
    path("amazon/",views.amazon, name='amazon'),
    path("rankuten/",views.rakuten, name='rakuten'),
    path("yahoo/",views.yahoo, name='yahoo'),

    # form
    path('search/form/', views.search_form, name='form'),
    path('carry/', views.carry, name='carry'),
    path('shoulder/', views.shoulder, name='shoulder'),
    path('toto/', views.toto, name='toto'),
    path('drop/', views.drop, name='drop'),
    path('netcloth/', views.netcloth, name='net'),
    path('bag/', views.bag, name='bag'),
    path('ryukku/', views.ryukku, name='ryukku'),
    path('reji_bag/', views.reji_bag, name='reji_bag'),
    path('reji/', views.reji, name='reji'),

    # price
    path("search/price/",views.search_price, name='price'),
    path('hund/', views.hund, name='hund'),
    path('two_hund/', views.two_hund, name='two_hund'),
    path('three_hund/', views.three_hund, name='three_hund'),
    path('four_hund/', views.four_hund, name='four_hund'),
    path('five_hund/', views.five_hund, name='five_hund'),
    path('over/', views.over, name='over'),

    # method
    path("search/method/",views.search_method, name='method'),
    path('natural/', views.natural, name='natural'),
    path("fold/", views.fold, name='fold'),
]
