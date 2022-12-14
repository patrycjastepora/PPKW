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

    def check_string(userStr):
        d = {"lowercase": 0, "uppercase": 0, "digits": 0, "special": 0}
        for c in userStr:
            if c.islower():
                d["lowercase"] += 1
            elif c.isupper():
                d["uppercase"] += 1
            elif c.isdigit():
                d["digits"] += 1
            elif any(not c.isalnum() for c in userStr):
                d["special"] += 1
            else:
                continue
        return json.dumps(d)

# --- main ---

PORT = 4080

print(f'Starting: http://localhost:{PORT}')

tcp_server = socketserver.TCPServer(("", PORT), web_server)
tcp_server.serve_forever()
