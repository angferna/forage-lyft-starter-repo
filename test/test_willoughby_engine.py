import unittest

from Engine.willoughby_engine import WilloughbyEngine


class TestWilloughbyEngine(unittest.TestCase):
    def test_willoughbyEngine_service_true(self):
        engine = WilloughbyEngine(9001, 0)
        self.assertTrue(engine.needs_service())

    def test_willoughbyEngine_service_false(self):
        engine = WilloughbyEngine(9000, 1)
        self.assertTrue(engine.needs_service())