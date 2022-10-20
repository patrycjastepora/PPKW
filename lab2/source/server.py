#!/usr/bin/env python3
import http.server
import socketserver
import os
import datetime

#print('source code for "http.server":', http.server.__file__)

class web_server(http.server.SimpleHTTPRequestHandler):
    
    def do_GET(self):

        print(self.path)
        
        if self.path == '/':
            self.protocol_version = 'HTTP/1.1'
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=UTF-8")
            self.end_headers()            
            self.wfile.write(b"Hello World!\n")

        elif self.path.startswith('/cmd'):
            self.protocol_version = 'HTTP/1.1'
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=UTF-8")
            self.end_headers()            

            if self.path.split('=')[1] == 'time':
                txt = time() + "\n"

            elif self.path.split('=')[1] == 'rev&str':
                txt = rev(self.path.split('='[2])) + "\n"

            else: 
               self.wfile.write(b"Hello World!\n")
            
            self.wfile.write(txt.encode(encoding='UTF-8'))
        else:
            super().do_GET()

    def time():
        return datetime.now().strftime("%H:%M:%S")
    
    def rev(userTxt): 
        s = ""
        for ch in userTxt:
            s = ch + s
        return s
# --- main ---

PORT = 4080

print(f'Starting: http://localhost:{PORT}')

tcp_server = socketserver.TCPServer(("",PORT), web_server)
tcp_server.serve_forever()
