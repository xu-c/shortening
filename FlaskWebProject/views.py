"""
Routes and views for the flask application.
"""

from flask import request
from FlaskWebProject import app
import urllib, urllib2, json


# API = 'http://dwz.cn/create.php'
API = 'http://is.gd/create.php'
ARG = 'url'
# KEY = 'tinyurl'
KEY = 'shorturl'

@app.route('/')
def shortening():
    url = request.values.get('url')
    if url:
        data = {}
        data[ARG] = url
        data['format'] = 'json'
        post_data = urllib.urlencode(data)
        req = urllib2.Request(API, post_data)
        res_data = urllib2.urlopen(req)
        return_data = json.load(res_data)

        if return_data.has_key(KEY):
            return return_data[KEY]
        else:
            return str(return_data)

    else:
        return 'Please visit /?url={url_long}'
