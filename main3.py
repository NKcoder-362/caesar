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
import webapp2
from caesar import  encrypt

form="""
<form method="post"  >
<label for "Rotate">Rotate by:
    <input name ="Rotate" type = "text">
</label>
<br>
<br>
<textarea type = "text" name="text"
          style="height:100px; width:400px;">{{text}}</textarea>
<br>
<br>
<input type = "submit" name = "Submit Query">
</form>
"""  # ends variable named form
class MainPage(webapp2.RequestHandler): #generic req handler from google
    def get(self):
        #self.response.headers['Content-Type'] = 'text/plain'
        self.response.write(form) #changed from printing "hello world"
                                    #to printing the form
    def post(self):
        Rotate = self.request.get("Rotate")
        self.response.out.write(Rotate)

app = webapp2.WSGIApplication([('/', MainPage)  ],# 1 URL '/', that maps to handler called MainPage
                                debug=True)  #this is the URL mapping section.
