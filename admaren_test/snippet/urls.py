from django.conf.urls import url
from snippet.views import *

urlpatterns = [
    url(r'^snippetAPI/',snippetAPI.as_view(), name='snippetAPI'),
    url(r'^tagAPI/',tagAPI.as_view(), name='tagAPI'),
    url(r'^tagDetailAPI/',tagDetailAPI.as_view(), name='tagDetailAPI'),
    url(r'^overallAPI/',overallAPI.as_view(), name='overallAPI'),
]
