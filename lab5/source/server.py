#!/usr/bin/env python3
from flask import Flask, request, jsonify

app=Flask(__name__)

def operation(num1, num2):
	return [num1+num2,num1-num2,num1*num2,num1//num2,num1%num2]
	
def check_str(userStr):
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
  	return d
  	
app.run(port=4080, host='0.0.0.0')
