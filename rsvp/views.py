from rest_framework import status
from rest_framework.decorators import api_view, throttle_classes
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, decorators, permissions, authentication
from rest_framework.response import Response

from rest_framework import filters
import random

from rest_framework import renderers
from rest_framework.reverse import reverse
from rest_framework import throttling
from rsvp.models import Rsvp, Guest
from rsvp.serializers import RsvpSerializer, GuestSerializer
from rsvp.permissions import IsOwner

from django.contrib.auth.models import User



class OncePerSecUserThrottle(throttling.UserRateThrottle):
        rate = '1/second'

class IsOwnerFilterBackend(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        pk = view.kwargs.get(view.lookup_field, None)
        method = request.method
        if (method in {'GET'} and pk is None):
            return queryset.filter(owner=request.user)
        else:
            return queryset

class RsvpViewSet(viewsets.ModelViewSet):
    queryset = Rsvp.objects.all()
    serializer_class = RsvpSerializer
    throttle_class = OncePerSecUserThrottle
    # throttle_classes = (OncePerSecUserThrottle)
    # filter_backends = (IsOwnerFilterBackend)
    # permission_classes = (permissions.IsAuthenticated, IsOwner)
    # authentication_classes = (authentication.SessionAuthentication, authentication.BasicAuthentication)

class GuestViewSet(viewsets.ModelViewSet):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer

    @decorators.detail_route(methods = ['get'])
    def byrsvp(self, request, pk):
        # queryset = Guest.objects.filter(rsvp_id = pk)
        queryset = Rsvp.objects.get(id = pk).guest_set.all()
        serializer = GuestSerializer(queryset, many = True)
        return Response(serializer.data)


