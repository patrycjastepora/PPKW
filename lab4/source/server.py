#!/usr/bin/env python3
from flask import Flask, request
import re

# print('source code for "http.server":', http.server.__file__)
app = Flask(__name__)

@app.route("/", methods=['GET'])
def input_numbers():
	return math_operations(request.args.get('num1'), request.args.get('num2'))

def math_operations(num1, num2):
	num1 = int(num1)
	num2 = int(num2)
	d = { "sum" : num1+num2, "sub" : num1-num2, "mul" : num1*num2, "div" : num1/num2, "mod" : num1%num2}
	return d
	
# --- main ---
if __name__ = '__main__':

	PORT = 4080

	print(f'Starting: http://localhost:{PORT}')
	
	app.run(debug=False,host='0.0.0.0',port=PORT)
	
