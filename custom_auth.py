#encoding=utf8

from requests.auth import AuthBase
import requests

class PizzaAuth(AuthBase):
    '''Attaches HTTP Pizza Authentication to the given Request object.'''
    def __init__(self, username):
        # setup any auth-related data here
        self.username = username

    def __call__(self, r):
        # modify and return the request
        r.headers['X-Pizza'] = self.username
        return r

print requests.get('http://pizzabin.org/admin', auth=PizzaAuth('kenneth'))