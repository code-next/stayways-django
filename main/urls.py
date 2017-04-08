from django.conf.urls import url,include

from . import views

urlpatterns=[
    url(r'^$',views.home.as_view(), name='index'),
    url(r'^login/$',views.login),
]