"""
Definition of urls for DjangoWebProject1.
"""

from datetime import datetime
from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin

import django.contrib.auth.views
import app.forms
import app.views


# Uncomment the next lines to enable the admin:
admin.autodiscover()

urlpatterns = [

    url(r'^recruters/(?P<id>\d+)$', app.views.recruters, name='recruters'),
    url(r'^sith$', app.views.sithLog, name='sithLog'),
    url(r'^quiz/(?P<id>\d+)$', app.views.takeAquiz, name='takeAquiz'),
    url(r'^recruters/subscribe$', app.views.recrutesubscribe, name='recrutesubscribe'),
    url(r'^recruters/(?P<Pid>\d+)/(?P<id>\d+)$', app.views.recrutesdetails, name='recrutesdetails'),
    url(r'^quiz/(?P<Pid>\d+)/vote/(?P<id>\d+)$', app.views.vote, name='vote'),
    url(r'^$', app.views.home, name='home'),
    url(r'^contact$', app.views.contact, name='contact'),
    url(r'^about$', app.views.about, name='about'),
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

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
  url(r'^admin/', include(admin.site.urls)),
]
