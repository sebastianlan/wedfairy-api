from rest_framework import viewsets, decorators, throttling, mixins
from rest_framework.response import Response
from rsvp.models import Rsvp, Guest
from rsvp.serializers import RsvpSerializer, GuestSerializer
from rsvp.permissions import IsAppAuthorized_rsvp, IsAppAuthorized_guest


class OncePerSecUserThrottle(throttling.UserRateThrottle):
        rate = '1/second'


class RsvpViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = Rsvp.objects.all()
    serializer_class = RsvpSerializer
    # throttle_classes = [OncePerSecUserThrottle]
    permission_classes = [IsAppAuthorized_rsvp]

    @decorators.detail_route(methods=['GET'], permission_classes=[IsAppAuthorized_guest])
    def guests(self, request, pk):
        # queryset = Guest.objects.filter(rsvp_id = pk)
        queryset = Rsvp.objects.get(id=pk).guest_set.all()
        serializer = GuestSerializer(queryset, many=True)
        return Response(serializer.data)


class GuestViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer




