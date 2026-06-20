import json


def add(a, b):
    return a + b


def divide(a, b):
    return a / b


def lambda_handler(event, context):
    body = event.get("body", event)
    if isinstance(body, str):
        try:
            body = json.loads(body)
        except json.JSONDecodeError as exc:
            raise ValueError("Request body must be valid JSON") from exc

    if not isinstance(body, dict):
        raise ValueError("Request body must be a JSON object")

    required_fields = ("a", "b", "operation")
    missing_fields = [field for field in required_fields if field not in body]
    if missing_fields:
        raise ValueError(
            f"Missing required fields: {', '.join(missing_fields)}"
        )

    a = body["a"]
    b = body["b"]
    operation = body["operation"]

    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Fields a and b must be numeric")

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
