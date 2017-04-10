from django.conf.urls import url,include

from . import views

urlpatterns=[
    url(r'^$', views.index, name='index'),
     url(r'^signup/',views.signup),
    url(r'^login/$',views.signin),
    url(r'^room/$',views.roomlistview),
    url(r'^addroom/$',views.AddRoom),
]