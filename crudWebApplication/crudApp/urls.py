from django.conf.urls import include, url
from .views import empList, empUpdate, empDel, home, newEmp

urlpatterns = [

    url(r'^$', home, name='home'),
    url(r'^list/$', empList, name='empList'),
    url(r'^newemp/$', newEmp, name='newEmp'),
    url(r'^update/(?P<id>\d+)/$', empUpdate, name='empUpdate'),
    url(r'^delete/(?P<id>\d+)/$', empDel, name='empDel'),

]
