from django.conf.urls import url
from django.urls import path, include

from pdb_app import views

urlpatterns = [
   url(r'^$', views.index, name='index'),
   url(r'^item/(?P<item_id>[0-9]+)', views.item, name = 'item'),
]