def add(a, b):
    return a + b

def divide(a, b):  
    return a / b

def multiply(a, b):
    return a * b

def lambda_handler(event, context):
    if "body" in event:
        if isinstance(event['body'], str):
            import json
            body = json.loads(event['body'])


    a = body['a']
    b = body['b']
    operation = body['operation']

    if operation == 'add':
        result = add(a, b)
    elif operation == 'divide':
        result = divide(a, b)
    else:
        raise ValueError("Unsupported operation")

    return {
        'statusCode': 200,
        'body': result
    }