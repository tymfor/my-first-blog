from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$',views.post_new, name = 'post_new'),
    url(r'^post/AHP_survey/$',views.AHP_survey, name = 'ahp_survey'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$',views.post_edit, name = 'post_edit'),
    url(r'^post/(?P<pk>[0-9]+)/delete/$',views.post_delete, name = 'post_delete'),
    url(r'^post/(?P<pk>[0-9]+)/mitigation_measures/$',views.mitigation_measures, name = 'mitigation_measures'),
    url(r'^about/$', views.post_about, name='post_about'),
    url(r'^account/signup/$', views.sign_up, name = 'sign_up'),
    url(r'^account/signup_ok/$', views.signup_ok, name='signup_ok'),

]
