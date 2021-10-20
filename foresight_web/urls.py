from django.conf.urls import include, url
from django.urls import path
from django.contrib import admin
from ctf.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^register$', register_view, name='register'),
    url(r'^login$', login_view, name='login'),
    url(r'^logout$', logout_view, name='logout'),
    url(r'^submit$', submit_view, name='submit'),
    url(r'^$', main_page, name='main_page'),
    path('<str:stage_name>', stage_view, name='stage'),
]
