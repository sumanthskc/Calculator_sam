import json

import requests
# import requests
def add(a,b):
    return a+b 
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b==0:
        return 0
    return a/b



def lambda_handler(event, context):
    
    a,b,op=int(event["a"]),int(event["b"]),str(event["op"])
    result=None
    ops = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
    }
    
    func=ops.get(op)
    if func:
        result=func(a,b)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Success",
            "result": f"{a} {op} {b} = {result}"
            
        }),
    }
