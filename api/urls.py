from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path("auth/", include("api.modules.auth.urls"), name='api.auth'),
    path("google-maps/", include("api.modules.google_maps.urls"),
         name='api.google_maps'),
]
