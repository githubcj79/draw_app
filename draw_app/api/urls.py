from django.urls import include, path
from . import views

urlpatterns = [
  path('welcome', views.welcome),
  path('addcompetitor', views.add_competitor),
  path('draw', views.do_draw)
]
