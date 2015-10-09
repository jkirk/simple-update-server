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
        'MySecondApplicatoin': '1.0.0',
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
        parsed_path = parse_qs(urlparse(s.path).query)
        s.wfile.write("Application;" + latestVersion("Application") + ";http://example.com/pub/update.zip")
        # s.wfile.write("AssetSheriff;2.5.2;http://192.168.0.65/pub/update.zip")
        # If someone went to "http://something.somewhere.net/foo/bar/",
        # then s.path equals "/foo/bar/".

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
