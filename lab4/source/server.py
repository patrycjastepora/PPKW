#!/usr/bin/env python3
import http.server
import socketserver
import os
import re
import json

# print('source code for "http.server":', http.server.__file__)

class web_server(http.server.SimpleHTTPRequestHandler):

    def do_GET(self):

        print(self.path)

        if self.path == '/':
            self.protocol_version = 'HTTP/1.1'
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=UTF-8")
            self.end_headers()
            self.wfile.write(b"Hello World!\n")
	elif self.path.startswith('/str='):
		temp = self.path.split(=)[1]
		temp = unquote(temp)
		self.wfile.write(bytes(checkStr(temp), encoding='UTF-8'))
        else:
            super().do_GET()

    def math_operations(num1, num2):
        num1 = int(num1)
        num2 = int(num2)
        d = { "sum" : num1+num2, "sub" : num1-num2, "mul" : num1*num2, "div" : num1/num2, "mod" : num1%num2}
        return json.dumps(d)

# --- main ---

PORT = 4080

print(f'Starting: http://localhost:{PORT}')

tcp_server = socketserver.TCPServer(("", PORT), web_server)
tcp_server.serve_forever()
