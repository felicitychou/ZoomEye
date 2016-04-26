import urllib,urllib2,json

def post(url,headers={},params=None):
    if params:
        data = json.dumps(params)
        req = urllib2.Request(url=url,data=data,headers=headers)
    else:
        req = urllib2.Request(url=url,headers=headers)
    response = urllib2.urlopen(req)
    return Response(response)

def get(url,headers={},params=None):
    if params:
        data = urllib.urlencode(params)
        url = url + '?' + data
        req = urllib2.Request(url=url,headers=headers)
    else:
        req = urllib2.Request(url=url,headers=headers)
    response = urllib2.urlopen(req)
    return Response(response)

class Response(object):
    def __init__(self,response):
        self.content = ""
        self.get_content(response)
        self.status_code = response.getcode()

    def get_content(self,response):
        for line in response.readlines():
            self.content += line

    def json(self):
        return json.loads(self.content)




