from rest_framework import permissions
import requests


class IsAppAuthorized_rsvp(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in {'GET', 'POST'}:
            return True
        pk = view.kwargs.get(view.lookup_field)
        app = 'rsvp'
        token = request.query_params.get('token')
        r = requests.post('http://api.wedfairy.com/api/appstore/authorize/',
                          data={'id': pk, 'app': app, 'token': token})
        if r.status_code == 200:
            return True
        else:
            return False


class IsAppAuthorized_guest(permissions.BasePermission):
    def has_permission(self, request, view):
        pk = view.kwargs.get(view.lookup_field)
        app = 'rsvp'
        token = request.query_params.get('token')
        r = requests.post('http://api.wedfairy.com/api/appstore/authorize/',
                          data={'id': pk, 'app': app, 'token': token})
        if r.status_code == 200:
            return True
        else:
            return False
