from django.conf.urls import url
from rango import views

urlpatterns = [
	url(r'^$', views.login, name='login'),
	url(r'^index/$', views.index, name='index'),
	url(r'^logout/$', views.logout, name='logout'),
]