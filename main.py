#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
#coding:utf-8
from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.ext.webapp import template
from google.appengine.api import users
from google.appengine.ext import db
import os
import cgi
class Greeting(db.Model):
  author = db.UserProperty()
  content = db.StringProperty(multiline=True)
  date = db.DateTimeProperty(auto_now_add=True)
class MainHandler(webapp.RequestHandler):
    def get(self):
        greetings_query = Greeting.all().order('-date')
        greetings = greetings_query.fetch(10)

        if users.get_current_user():
          url = users.create_logout_url(self.request.uri)
          url_linktext = 'Logout'
        else:
          url = users.create_login_url(self.request.uri)
          url_linktext = 'Login'
        template_values = {
            'greetings': greetings,
            'url': url,
            'url_linktext': url_linktext,
            }
        path = os.path.join(os.path.dirname(__file__), 'mainpage.txt')
        self.response.out.write(template.render(path, template_values))
class log_in(webapp.RequestHandler):
    def get(self):
        greeting = Greeting()

        if users.get_current_user():
            greeting.author = users.get_current_user()
            greeting.content = self.request.get('content')
            greeting.put()
        self.redirect('/')
##class DATA_csieA(db.Model):
##    name = db.StringProperty()
##    account = db.UserProperty()
##    total_points = db.FloatProperty()
##    total_assists = db.FloatPrpperty()
##    total_rebounds = db.FloatProprty()
##    total_steals = db.FloatProperty()
##    toatl_blocks = db.FLoatProperty()
##    toatl_turnovers = db.FloatProperty()
##    total_threeattempt = db.FloatProperty()
##    total_threemade = db.FloatProperty()
##    total_fouls = db.FloatProperty()
##    FieldGoal_made = db.FloatProperty()
##    FieldGoal_attempt = db.FloatProperty()
##    FreeThrow_made = db.FLoatProperty()
##    FreeThrow_attempt = db.FLoatProperty()

class datakeyin(webapp.RequestHandler):
    def post(self):
        database=DATA_csieA()
        database.name=self.request.get('name')
        database.total_points=database.total
class test(webapp.RequestHandler):
    def get(self):
        template_values = {
            'greetings': greetings,
            'url': url,
            'url_linktext': url_linktext,
            }
        path = os.path.join(os.path.dirname(__file__), 'test.txt')
        self.response.out.write(template.render(path, template_values))   
class test2(webapp.RequestHandler):
    def get(self):
        template_values = {
            }
        path = os.path.join(os.path.dirname(__file__), 'test2.txt')
        self.response.out.write(template.render(path, template_values))    
    

def main():
    application = webapp.WSGIApplication([('/', MainHandler),('/test2',test2),('/test',test),('/sign',log_in)],
                                         debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
