from django.conf.urls import include, url
from django.contrib import admin
from ctf.views import *

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^register$', register_view, name='register'),
    url(r'^login$', login_view, name='login'),
    url(r'^logout$', logout_view, name='logout'),
    url(r'^submit$', submit_view, name='submit'),
    url(r'^$', main_page, name='main_page'),
]
