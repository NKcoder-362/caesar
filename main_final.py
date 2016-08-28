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
from caesar import  encrypt  # used to encrypt data
import cgi           # used to escape bad input from user

form="""
<form method="post"  >
<label for "rotate">Rotate by:
    <input name ="rotate" type = "text" value = "%(rotate)s">
</label>
<br>
<br>
<textarea type = "text" name="raw"
          style="height:100px; width:400px;">%(raw)s</textarea>
<br>
<br>
<input type = "submit" name = "Submit Query">

</form>
"""  # ends variable named form
class MainPage(webapp2.RequestHandler): #generic req handler from google

    def formwrite(self, rotate="", raw=""):  # sets var default values to ""
        replacements = {"rotate" : rotate, "raw" : raw} # dictionary - replace "" w/user input
        self.response.write(form % replacements)

#create write form function
#should accept form , and rotate and text as parameters with empty default values

    def get(self):
        self.formwrite()

    def post(self):
        rotate = self.request.get("rotate")
        raw = self.request.get("raw")

        if not rotate.isdigit():   #validate rotate as number
            self.response.write ("Rotate must be a number")
            return
        rotate = int(rotate)

        raw = cgi.escape(raw)  #any bad data entered into the textarea called raw
                                #will be "escaped"(turned into plain text)
        result = encrypt(raw,rotate)  # this calls the function encrypt,
                                    #the data entered into the form fields raw,rotate
                                    #are put into the required parameters for the function
                                    #and returns encrypted text into the text area called raw
        self.formwrite(rotate, result)

#get text from text area
#escape text area text ie text_area_text = cgi.escape(text_area_text)
#call encrypt using rotate
#call write form function with rotate and encrypted text passed in
#        self.response.out.write(rotate)


app = webapp2.WSGIApplication([('/', MainPage)  ],# 1 URL '/', that maps to handler called MainPage
                                debug=True)  #this is the URL mapping section.
