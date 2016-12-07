#!/usr/bin/env python
# coding=utf-8

#import urllib.request, urllib.parse, urllib.error, json

import json
import sys

py_version = sys.version_info[0]
if  py_version== 3:
    from urllib import request, parse, error
elif py_version == 2:
    import urllib,urllib2
else:
    print("Python version is not 2 or 3.")
    sys.exit(0)


def post(url,headers={},params=None):

    if  py_version== 3:
        if params:
            data = json.dumps(params)
            data = bytes(data,'utf8')  
            req = request.Request(url=url,data=data,headers=headers)
        else:
            req = request.Request(url=url,headers=headers)
        response = request.urlopen(req)
        return Response(response)
    elif py_version == 2:
        if params:
            data = json.dumps(params)
            req = urllib2.Request(url=url,data=data,headers=headers)
        else:
            req = urllib2.Request(url=url,headers=headers)
        response = urllib2.urlopen(req)
        return Response(response)
    else:
        return None

def get(url,headers={},params=None):

    if sys.version_info[0] == 3:
        if params:
            data = parse.urlencode(params)
            url = "%s?%s" % (url, data)
            req = request.Request(url=url,headers=headers)
        else:
            req = request.Request(url=url,headers=headers)
        response = request.urlopen(req)
        return Response(response)
    elif sys.version_info[0] == 2:
        if params:
            data = urllib.urlencode(params)
            url = url + '?' + data
            req = urllib2.Request(url=url,headers=headers)
        else:
            req = urllib2.Request(url=url,headers=headers)
        response = urllib2.urlopen(req)
        return Response(response)
    else:
        return None

class Response(object):
    def __init__(self,response):
        if sys.version_info[0] == 3:
            self.content = response.read().decode('utf-8')
            self.status_code = response.status
        elif sys.version_info[0] == 2:
            self.content = response.read()
            self.status_code = response.getcode()
        else:
            self.content = ""
            self.status_code = 404

    def json(self):
        return json.loads(self.content)




