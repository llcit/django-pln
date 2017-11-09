from django.conf.urls import patterns, url
from .views import *

app_name = 'pln'

urlpatterns = patterns('pln.views',
    #index view
    url(r'^$', index, name='index'),

)
