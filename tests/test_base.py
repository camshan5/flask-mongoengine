"""Tests for base MongoEngine class."""
from flask_mongoengine import MongoEngine
import pytest


def test_mongoengine_class__should_raise_type_error__if_config_not_dict():
    """MongoEngine will handle None values, but will pass anything else as app."""
    with pytest.raises(TypeError) as error:
        input_value = "Not dict type"
        MongoEngine(input_value)
    assert str(error.value) == "Invalid Flask application instance"


@pytest.mark.parametrize("input_value", [None, "Not dict type"])
def test_init_app__should_raise_type_error__if_config_not_dict(input_value):
    db = MongoEngine()
    with pytest.raises(TypeError) as error:
        db.init_app(input_value)
    assert str(error.value) == "Invalid Flask application instance"
