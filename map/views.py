from rest_framework import viewsets, throttling
from map.models import Map
from map.serializers import MapSerializer

class OncePerSecUserThrottle(throttling.UserRateThrottle):
        rate = '1/second'

class MapViewSet(viewsets.ModelViewSet):
    queryset = Map.objects.all()
    serializer_class = MapSerializer
    throttle_class = OncePerSecUserThrottle