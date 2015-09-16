from rest_framework import permissions
import requests
from poll.models import Option


class IsAppAuthorized_poll(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in {'GET', 'POST'}:
            return True
        pk = view.kwargs.get(view.lookup_field)
        app = 'poll'
        token = request.query_params.get('token')
        r = requests.post('http://api.wedfairy.com/api/appstore/authorize/',
                          data={'id': pk, 'app': app, 'token': token})
        if r.status_code == 200:
            return True
        else:
            return False


class IsAppAuthorized_poll_vote(permissions.BasePermission):
    def has_permission(self, request, view):
        pk = view.kwargs.get(view.lookup_field)
        app = 'poll'
        token = request.query_params.get('token')
        r = requests.post('http://api.wedfairy.com/api/appstore/authorize/',
                          data={'id': pk, 'app': app, 'token': token})
        if r.status_code == 200:
            return True
        else:
            return False


class IsAppAuthorized_option_vote(permissions.BasePermission):
    def has_permission(self, request, view):
        option_id = view.kwargs.get(view.lookup_field)
        option = Option.objects.get(pk=option_id)
        pk = option.poll_id
        app = 'poll'
        token = request.query_params.get('token')
        r = requests.post('http://api.wedfairy.com/api/appstore/authorize/',
                          data={'id': pk, 'app': app, 'token': token})
        if r.status_code == 200:
            return True
        else:
            return False