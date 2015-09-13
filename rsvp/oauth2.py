
class OAuth2AuthExchangeError(Exception):
    def __init__(self, code, description):
        self.code = code
        self.description = description

    def __str__(self):
        return '%s: %s' % (self.code, self.description)


class OAuth2Request(object):

    def __init__(self, api):
        self.api = api
        self.host = 'api.wedfairy.com/api/appstore/authorize/'

    def post_request(self, token=None, app=None, id=None, scope=None, state=None):
        auth_params = {
            "token": token,
            "app": "rsvp",
            "id": id
        }
        return self.make_request(self.prepare_request("POST"))




