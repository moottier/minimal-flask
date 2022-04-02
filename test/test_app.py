import unittest
from flask import Blueprint, Flask
from app.app import create_app, register_blueprints
from app.config import TestingConfig

test_blueprint = Blueprint(
            name = 'test_blueprint', 
            import_name='__name__',
            url_prefix='/', 
        )

@test_blueprint.route('/')
def test_route():
    pass

class MockRoutesValid:
    def __init__(self):
        self.blueprint_1 = test_blueprint

class MockRoutesInvalid:
    def __init__(self):
        self.route_1 = dict()


def get_app_with_valid_blueprint_in_routes():
    return create_app("TestAppValidBlueprints", TestingConfig, MockRoutesValid())

def get_app_with_invalid_blueprint_in_routes():
    return create_app("TestAppInvalidBlueprints", TestingConfig, MockRoutesInvalid())


class TestRegisterBluePrints(unittest.TestCase):
    def test_production_register_blueprints_registers_valid_blueprints(self):
        app  = Flask("TestApp")

        expected_endpoint = 'test_blueprint.test_route'
        
        register_blueprints(app, MockRoutesValid())
        self.assertIn(
                expected_endpoint, 
                [rule.endpoint for rule in app.url_map.iter_rules()]
            )

    def test_production_register_blueprints_doesnt_register_invalid_blueprints(self):
        app_no_blueprints  = Flask("TestAppNoBlueprints")
        app_invalid_blueprints  = Flask("TestAppInvalidBlueprints")

        register_blueprints(app_invalid_blueprints, MockRoutesInvalid())

        app_no_bp_endpoints = [rule.endpoint for rule in app_no_blueprints.url_map.iter_rules()]
        app_inv_bp_endpoints = [rule.endpoint for rule in app_invalid_blueprints.url_map.iter_rules()]
        
        self.assertTrue(
            set(app_no_bp_endpoints) == set(app_inv_bp_endpoints) 
            and len(app_no_bp_endpoints) == len(app_inv_bp_endpoints)
        )
