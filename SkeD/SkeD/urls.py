"""
Definition of urls for SkeD.
"""

from django.conf.urls import url, include
import django.contrib.auth.views
from django.contrib import admin, admindocs
from django.views.generic import ListView, DetailView
from datetime import datetime

import app.forms
import app.views
import SkillApp.views
from SkillApp.models import *

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', app.views.home, name='home'),
    url(r'^contact$', app.views.contact, name='contact'),
    url(r'^about', app.views.about, name='about'),
    url(r'^$', ListView.as_view(queryset=Applicant.objects.all().order_by('-LastName')[:25],
                                      template_name='app/new_about.html')),
    url(r'^login/$',
        django.contrib.auth.views.login,
        {
            'template_name': 'app/login.html',
            'authentication_form': app.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Log in',
                'year': datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),
    url(r'^findSkill/$', ListView.as_view(queryset=Applicant.objects.all().order_by('-LastName')[:25],
                                      template_name="SkillApp/FindSkill.html")),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
]