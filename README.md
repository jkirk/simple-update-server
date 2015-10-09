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

## License

The MIT License (MIT)

Copyright (c) 2015 Darshaka Pathirana

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

