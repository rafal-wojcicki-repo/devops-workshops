import json


def add(a, b):
    return a + b


def divide(a, b):
    return a / b


def lambda_handler(event, context):
    body = event.get("body", event)
    if isinstance(body, str):
        body = json.loads(body)

    a = body["a"]
    b = body["b"]
    operation = body["operation"]

    if operation == "add":
        result = add(a, b)
    elif operation == "divide":
        result = divide(a, b)
    else:
        raise ValueError("Unsupported operation")

    return {
        "statusCode": 200,
        "body": result,
    }
