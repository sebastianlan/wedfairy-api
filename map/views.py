from rest_framework import viewsets, throttling, mixins
from map.models import Map
from map.serializers import MapSerializer
from map.permissions import IsAppAuthorized


class OncePerSecUserThrottle(throttling.UserRateThrottle):
        rate = '1/second'


class MapViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = Map.objects.all()
    serializer_class = MapSerializer
    # throttle_classes = [OncePerSecUserThrottle]
    permission_classes = [IsAppAuthorized]
