# simple-update-server

I needed a simple web server which returns the latest version number of a
requested application. The HTTP request looks like this:

  http://$SERVER/?app=$APPLICATION

The respone will then look like this:

  $APPNAME;$APPVERSION;$DOWNLOADURL

The simple-update-server is based on BaseHTTPServer example taken from here:
https://wiki.python.org/moin/BaseHttpServer

The server also shows how to simply parse GET-parameters.

## Disclaimer

Please be aware that the simple-update-server is just a quick and dirty
implementation and should not be used in any production environment. The main
purpose of the project is to show some examples of how to use some python
functions.

