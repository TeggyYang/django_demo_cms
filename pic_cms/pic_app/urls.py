from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index_view, name='index'),
    url(r'^list/$', views.items_detail_view, name='items_detail'),
    url(r'^pic_detail_view/', views.pic_detail_view, name='pic_detail_view'),
    url(r'^pic_detail_view_update/', views.pic_detail_view_update, name='pic_detail_view_update'),
    url(r'^pic_detail_update/', views.pic_detail_update, name='pic_detail_update'),
    url(r'^pic_detail_delete/', views.pic_detail_delete, name='pic_detail_delete'),
    url(r'^add/', views.pic_detail_add, name='pic_detail_add'),
    url(r'^list/checked/$', views.items_checked_view, name='items_checked'),
    url(r'^list/unchecked/$', views.items_unchecked_view, name='items_unchecked'),
    url(r'^list/valid/$', views.items_valid_view, name='items_valid'),
    url(r'^list/unvalid/$', views.items_unvalid_view, name='items_unvalid'),
    url(r'^filter/$', views.items_filter, name='items_filter'),
    ]

