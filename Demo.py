import ZoomEye

def main(username,password):
    z = ZoomEye.ZoomEye(username, password)
    if z.login():
        if z.resourcesinfo():
            print z.response()
        else:
            print z.error()
        if z.hostsearch(query="port:80 nginx"):
            print z.response()
        else:
            print z.error()
        if z.websearch(query="wordpress"):
            print z.response()
        else:
            print z.error()
    else:
        print z.error()

if __name__ == '__main__':
    main(username='',password='')