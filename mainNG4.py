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
import cgi

form="""
<form method="post"  >
<label for "Rotate">Rotate by:
    <input name ="rotate" type = "number" value = "%(rotate)s">
</label>
<br>
<br>
<textarea type = "text" name="text"
          style="height:100px; width:400px;">{%(text)s}</textarea>
<br>
<br>
<input type = "submit" name = "Submit Query">
</form>
"""  # ends variable named form
class MainPage(webapp2.RequestHandler): #generic req handler from google
#create write form function
#should accept form , and rotate and text as parameters with empty default values

#auto changes example to abc if nothing is provided
    def get(self, example = "abc"):
        #self.response.headers['Content-Type'] = 'text/plain'
        self.response.write(form) #changed from printing "hello world"
                                    #to printing the form
    def post(self):
        rotate = self.request.get("rotate")
        text = self.request.get ("text")
        rotate = int(rotate)
        answer = encrypt(text,rotate)
        close = cgi.escape(answer)
        self.response.write(form % {"text":answer})

#validate rotate as number
#get text from text area
#escape text area text ie text_area_text = cgi.escape(text_area_text)
#call encrypt using rotate
#call write form function with rotate and encrypted text passed in
#        self.response.out.write(rotate)

app = webapp2.WSGIApplication([('/', MainPage)  ],# 1 URL '/', that maps to handler called MainPage
                                debug=True)  #this is the URL mapping section.
