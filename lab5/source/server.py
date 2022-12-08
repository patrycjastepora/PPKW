#!/usr/bin/env python3
from flask import Flask, request, jsonify

app=Flask(__name__)

def operation(num1, num2):
	return [num1+num2,num1-num2,num1*num2,num1//num2,num1%num2]
	
	
app.run(port=4080, host='0.0.0.0')
