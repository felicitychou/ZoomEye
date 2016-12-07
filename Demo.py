#!/usr/bin/env python
# coding=utf-8
# ZoomEye_use_requests support python 2 and 3

import sys

#from ZoomEye_use_requests import *
from ZoomEye import *

HostSearchFacets = "app,device,service,os,port,country,city"
WebSearchFacets = "webapp,component,framework,frontend,server,waf,os,country,city"

def main(username,password):
    '''init class ZoomEye with username and password'''
    z = ZoomEye(username, password)
    '''login '''
    if z.login():
        '''get resouresinfo'''
        if z.resourcesinfo():
            print("resouresinfo:")
            print(z.response())
        else:
            print(z.error())
        '''hostsearch(query,pages = 1,facets = '')'''
        if z.hostsearch(query="port:80 nginx"):
            print("hostsearch:")
            print(z.response())
        else:
            print(z.error())
        '''websearch(query,pages = 1,facets = '')'''
        if z.websearch(query="wordpress",facets='os'):
            print("websearch:")
            print(z.response())
        else:
            print(z.error())
    else:
        print(z.error())

if __name__ == '__main__':
    #main(username='',password='')
    if sys.version_info[0] == 3:
        username = input('Please input your username:')
        password = input('Please input your password:')
        main(username=username,password=password)
    elif sys.version_info[0] == 2:
        username = raw_input('Please input your username:')
        password = raw_input('Please input your password:')
        main(username=username,password=password)
    else:
        print("Python version is not 2 or 3.")
        sys.exit(0)

    