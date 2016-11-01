"""ux URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
#from django.contrib import admin

from CavTutor import views, auth_logic
from CavTutor import institution_views

urlpatterns = [
#    url(r'^admin/', include(admin.site.urls)),
    url(r'^institutions/(?P<inst_id>\d+)/?$', institution_views.detail),
    url(r'^institutions/?$', institution_views.listings),
    url(r'^institutions/create/?$', institution_views.create),

    url(r'^courses/(?P<course_id>\d+)/?$', views.course_detail),
    url(r'^courses/?$', views.course_list),

    url(r'^tutors/(?P<tutor_id>\d+)/?$', views.tutor_detail),
    url(r'^tutors/?$', views.tutor_list),

    url(r'^tutees/(?P<tutee_id>\d+)/?$', views.tutee_detail),
    url(r'^tutees/?$', views.tutee_list),

    url(r'^users/(?P<user_id>\d+)/?$', views.user_detail),
    url(r'^users/?$', views.user_list),
    
    url(r'^login/?$', auth_logic.login),
    url(r'^register/?$', auth_logic.register),
    url(r'^logout/?$', auth_logic.logout),
    url(r'^validate/?$', auth_logic.validate_user_cookie),
]
