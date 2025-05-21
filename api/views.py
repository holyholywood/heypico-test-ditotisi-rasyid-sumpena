from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.modules.google_maps.views import (
    places as google_maps_places,
    place_nearby as google_maps_place_nearby,
    directions as google_maps_directions,
    distance_matrixs as google_maps_distance_matrixs,
)
