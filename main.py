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
import os
import cgi
class MainHandler(webapp.RequestHandler):
    def get(self):
        template_values = {
            "a":[1,2,5,7]
            }
        path = os.path.join(os.path.dirname(__file__), 'mainpage.txt')
        self.response.out.write(template.render(path, template_values))
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
            "a":[1,2,5,7]
            }
        path = os.path.join(os.path.dirname(__file__), 'test.txt')
        self.response.out.write(template.render(path, template_values))   
    
    

def main():
    application = webapp.WSGIApplication([('/', MainHandler),('/test',test)],
                                         debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
