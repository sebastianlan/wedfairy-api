from rest_framework import permissions
import requests


class IsAppAuthorized(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in {'GET', 'POST'}:
            return True
        pk = view.kwargs.get(view.lookup_field)
        app = 'map'
        token = request.query_params.get('token')
        # print pk, app, token
        r = requests.post('http://api.wedfairy.com/api/appstore/authorize/',
                          data={'id': pk, 'app': app, 'token': token})
        if r.status_code == 200:
            return True
        else:
            return False
