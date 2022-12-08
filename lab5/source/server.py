#!/usr/bin/env python3
from flask import Flask, request, jsonify

app=Flask(__name__)

def operations(num1: int, num2: int):
    d = {"sum": 0, "sub": 0, "mul": 0, "div": 0, "mod": 0}
    d["sum"] = num1+num2
    d["sub"] = num1-num2
    d["mul"] = num1*num2
    d["div"] = num1//num2
    d["mod"] = num1%num2
    return d
	
def check_str(userStr: str):
    d = {"lowercase": 0, "uppercase": 0, "digits": 0, "special": 0}
    for c in userStr:
        if c.islower():
            d["lowercase"]+=1
        elif c.isupper():
            d["uppercase"]+=1
        elif c.isdigit():
            d["digits"]+=1
        elif any(not c.isalnum() for c in userStr):
            d["special"]+=1
        else:
            continue
    return d

@app.post('/')
def return_statistics():
    outNumbers = {}
    outStr = {}
    output = request.json
    if 'num1' in output and 'num2' in output:
        outNumbers = operations(output['num1'], output['num2'])
    if 'str' in output:
        outStr = check_str(output['str'])
    return {**outStr, **outNumbers}
	
app.run(port=4080, host='0.0.0.0')
