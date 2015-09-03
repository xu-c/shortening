"""
Routes and views for the flask application.
"""

from flask import request
from FlaskWebProject import app
import urllib, urllib2, json

@app.route('/')
def shortening():
    url = request.args.get('url')
    if url:
        api = 'http://dwz.cn/create.php'
        data = {}
        data['url'] = url
        post_data = urllib.urlencode(data)
        req = urllib2.Request(api, post_data)
        res_data = urllib2.urlopen(req)
        return_data = json.load(res_data)

        if return_data.has_key('tinyurl'):
            return return_data['tinyurl']
        else:
            return str(return_data)

    else:
        return 'Please visit /?url={url_long}'
