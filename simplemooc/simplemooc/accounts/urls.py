from django.conf.urls import url
from django.contrib.auth.views import login
from . import views

urlpatterns = [
    url(r'^entrar$', login, {'template_name': 'accounts/login.html'}, name='login'),
]
