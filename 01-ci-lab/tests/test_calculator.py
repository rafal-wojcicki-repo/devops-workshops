import json

import pytest

from app.calculator import add, divide, lambda_handler


def test_add():
    assert add(2, 3) == 5


def test_divide():
    assert divide(10, 2) == 5


def test_lambda_handler_accepts_direct_event():
    response = lambda_handler({"a": 2, "b": 3, "operation": "add"}, None)

    assert response == {"statusCode": 200, "body": 5}


def test_lambda_handler_accepts_json_body():
    response = lambda_handler(
        {"body": json.dumps({"a": 10, "b": 2, "operation": "divide"})},
        None,
    )

    assert response == {"statusCode": 200, "body": 5}


def test_lambda_handler_rejects_missing_fields():
    with pytest.raises(ValueError, match="Missing required field: operation"):
        lambda_handler({"a": 10, "b": 2}, None)


def test_lambda_handler_propagates_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        lambda_handler({"a": 10, "b": 0, "operation": "divide"}, None)


def test_lambda_handler_rejects_unsupported_operation():
    with pytest.raises(ValueError, match="Unsupported operation"):
        lambda_handler({"a": 10, "b": 2, "operation": "subtract"}, None)


def test_lambda_handler_rejects_invalid_json():
    with pytest.raises(ValueError, match="Request body must be valid JSON"):
        lambda_handler({"body": "{not-json"}, None)


def test_lambda_handler_rejects_non_numeric_values():
    with pytest.raises(TypeError, match="Fields a and b must be numeric"):
        lambda_handler({"a": "10", "b": 2, "operation": "add"}, None)
