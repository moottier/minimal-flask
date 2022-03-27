import unittest
from app.config import ProductionConfig, TestingConfig

class TestProductionConfig(unittest.TestCase):
    def setUp(self):
        self.config = ProductionConfig()

    def test_production_config_defaults_to_debug_false(self):
        self.assertFalse(self.config.DEBUG)

    def test_production_config_defaults_to_testing_false(self):
        self.assertFalse(self.config.TESTING)

    def test_production_config_defaults_to_env_production(self):
        self.assertEqual(self.config.ENV, 'production')

class TestTestingConfig(unittest.TestCase):
    def setUp(self):
        self.config = TestingConfig()

    def test_production_config_defaults_to_debug_true(self):
        self.assertTrue(self.config.DEBUG)

    def test_production_config_defaults_to_testing_true(self):
        self.assertTrue(self.config.TESTING)

    def test_production_config_defaults_to_env_production(self):
        self.assertEqual(self.config.ENV, 'production')
