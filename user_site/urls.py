from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.error_category, name='error_category'),
    url(r'^$', views.error_appearance, name='error_appearance'),
    url(r'^$', views.solution, name='solution'),
]