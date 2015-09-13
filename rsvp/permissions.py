from rest_framework import permissions
from rsvp.models import Rsvp

class IsOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        ip_addr = request.META['REMOTE_ADDR']
        blacklisted = Rsvp.objects.filter(ip_addr=ip_addr).exists()
        return not blacklisted
