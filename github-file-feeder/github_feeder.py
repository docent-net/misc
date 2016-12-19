#!/usr/bin/python

import feedparser

import webapp2


class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('main page')


class TestRouteHandler(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('testroute')


class AnotherRouteHandler(webapp2.RequestHandler):
    def another(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('anotherroute')
routes = [
    ('/', MainPage),
    ('/testroute', TestRouteHandler),
    webapp2.Route(
        r'/another',
        handler=AnotherRouteHandler,
        handler_method='another',
        methods=['GET']
    )
]

config = dict()
# config['template.dir'] = 'templates/'
# config['assets.dir'] = 'assets/'
config['webapp2_extras.sessions'] = {'secret_key': 'mysupersecretkey'}
# http://johnpfeiffer.bitbucket.org/uwsgi-install-webapp2-post-password/
application = webapp2.WSGIApplication(routes=routes, debug=True, config=config)
