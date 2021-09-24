from django.conf.urls import url
from user_login.views import *

urlpatterns = [
    url(r'^login/',loginCheck.as_view(), name='login'),
    url(r'^user_register/',UserRegistration.as_view(),name='UserRegisteration'),
]
