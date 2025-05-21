from rest_framework.decorators import api_view, permission_classes, throttle_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .services import services
from api.utils.throttle import get_throttle_class


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@throttle_classes([get_throttle_class('10/hour')])
def places(request):
    query = request.GET.get('search', None)
    return Response(services().get_place(request.GET))


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@throttle_classes([get_throttle_class('20/hour')])
def place_nearby(request):
    return Response(services().get_place_nearby(request.GET))


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@throttle_classes([get_throttle_class('10/hour')])
def directions(request):
    return Response(services().get_directions(request.GET))


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@throttle_classes([get_throttle_class('15/hour')])
def distance_matrixs(request):
    return Response(services().get_distance_matrix(request.GET))
