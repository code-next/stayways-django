from django.conf.urls import url,include

from . import views

urlpatterns=[
    url(r'^$', views.index, name='index'),
    url(r'^signup/',views.signup),
    url(r'^login/$',views.signin),
    url(r'^room/$',views.roomlistview),
    url(r'^addroom/$',views.AddRoom),
    url(r'^addreview/$',views.AddReview),
    url(r'^dashboard',views.dashboard),
    url(r'^room/(?P<rid>[0-9]+)/$', views.room_detail),
    url(r'^logout/$',views.logout_view),
    url(r'^ajax/get_city/$',views.ajax_getCity,name="ajax_getCity"),
    url(r'^ajax/roomfilter/$',views.ajax_roomfilter),
]