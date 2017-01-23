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
import random

def getRandomFortune():

    fortunes= [
        "You will find a bushel of money",
        "Your smile will tell you what makes you feel good.",
        "Don't panic",
        "You will find a thing. It may be important",
        "Your reality check is about to bounce.",
        "Stop eating now. Food poisoning no fun."
    ]


    index = random.randint(0,5)

    return fortunes[index]

class MainHandler(webapp2.RequestHandler):
    def get(self):
        header = "<h1>Fortune Cookie</h1>"

        fortune = "<strong>" + getRandomFortune() + "</strong>"
        fortune_sentence = "Your fortune: " + fortune
        fortune_paragraph= "<p>" + fortune_sentence + "</p>"


        lucky_number = "<strong>" + str(random.randint(1,100)) + "</strong>"
        number_sentence = "Your lucky number: " + lucky_number
        number_paragraph = "<p>" + number_sentence + "</p>"

        cookie_again_button = "<a href='.'><button>Another cookie plz!</button></a>"

        content = header + fortune_paragraph + number_paragraph + cookie_again_button

        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
