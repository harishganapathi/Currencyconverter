from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^.*signup$', views.signup, name='signup'),
    url(r'^.*signin$', views.signin, name='signin'),
    url(r'^.*signout/$', views.signout, name="signout"),
    url(r'^.*landingpage/$', views.landingpage, name="landingpage"),
    #url(r'^.*conversion/$', views.conversion, name="conversion"),
    #url(r'')
]
