from django.urls import path

from .views import *


urlpatterns = [
    path('', view_all, name="home"),
    path("services/", service_by_category, name='services'),
    path('detail/', service_detail, name="detail"),
    path('mechanics/', servise_by_mechanic, name="mechanics")
]