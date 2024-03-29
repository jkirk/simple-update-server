"""
Responding with an HTML Page

Source: https://wiki.python.org/moin/BaseHttpServer

"""

import time
import BaseHTTPServer
from urlparse import urlparse, parse_qs


HOST_NAME = '0.0.0.0' # !!!REMEMBER TO CHANGE THIS!!!
PORT_NUMBER = 9999 # Maybe set this to 9000.

def latestVersion(appName):
    return {
        'MyFirstApplication': '2.6.2',
        'MySecondApplication': '1.0.0',
    }.get(appName, '')

def downloadUrl(appName):
    return {
        'MyFirstApplication': 'http://example.com/pub/app1-update.zip',
        'MySecondApplication': 'http://example.com/pub/app2-update.zip',
    }.get(appName, '')

class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_HEAD(s):
        s.send_response(200)
        s.send_header("Content-type", "text/plain")
        s.end_headers()
    def do_GET(s):
        """Respond to a GET request."""
        s.send_response(200)
        s.send_header("Content-type", "text/plain")
        s.end_headers()
        params = parse_qs(urlparse(s.path).query)
        if params.get('app', '') == '':
            s.wfile.write('go away')
        else:
            appName = params.get('app', '')[0]
            appVersion = latestVersion(appName)
            appDownloadUrl = downloadUrl(appName)
            if appVersion == '' or appDownloadUrl == '':
                s.wfile.write('')
            else:
                s.wfile.write(appName + ";" + appVersion + ";" + appDownloadUrl)

if __name__ == '__main__':
    server_class = BaseHTTPServer.HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
    print time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER)
