import requests

HostSearchFacet = "app,device,service,os,port,country,city"
WebSearchFacet = "webapp,component,framework,frontend,server,waf,os,country,city"

class ZoomEye(object):

    def __init__(self,username,password):
       """
       :type username: str
       :type password: str

       """
       self.username = username
       self.password = password
       self.access_token = "JWT "
       self.r = None


    def requestisok(self):
       if self.r.status_code == requests.codes.ok:
           return True
       else:
           return False

    def error(self):
       json = self.r.json()
       return str(self.r.status_code) + "\n" + json['error'] + "\n" + json['message'] + "\n" + json['url'] + "\n"

    def payload(self,query,page,facet):
        if facet == "":
            return {'query': query, 'page': page}
        else:
            return {'query': query, 'page': page, 'facet': facet}

    def login(self):
       self.r = requests.post('http://api.zoomeye.org/user/login',json={"username":self.username,"password":self.password})
       if self.requestisok():
           self.access_token += self.r.json()['access_token']
           return True
       else:
           return False

    def resourcesinfo(self):
       headers = {'Authorization': self.access_token}
       self.r = requests.get('http://api.zoomeye.org/resources-info', headers=headers)
       return self.requestisok()

    def hostsearch(self,query,page = 1,facet = HostSearchFacet):
       headers = {'Authorization': self.access_token}
       payload = self.payload(query, page, facet)
       self.r = requests.get("http://api.zoomeye.org/host/search", headers=headers, params=payload)
       return self.requestisok()

    def websearch(self,query,page = 1,facet = WebSearchFacet):
       headers = {'Authorization': self.access_token}
       payload = self.payload(query,page,facet)
       self.r = requests.get("http://api.zoomeye.org/web/search", headers=headers, params=payload)
       return self.requestisok()

    def response(self):
        return self.r.json()

