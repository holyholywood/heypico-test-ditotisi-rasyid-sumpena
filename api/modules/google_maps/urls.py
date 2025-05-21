from api.views import google_maps_places, google_maps_place_nearby, google_maps_directions, google_maps_distance_matrixs
from django.urls import path

urlpatterns = [
    path('places/find', google_maps_places, name='api.google_maps_places'),
    path('places/nearby', google_maps_place_nearby,
         name='api.google_maps_place_nearby'),
    path('directions', google_maps_directions,
         name='api.google_maps_directions'),
    path('distance-matrix', google_maps_distance_matrixs,
         name='api.google_maps_distance_matrixs'),
]
