import unittest
from unittest.mock import MagicMock

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


from spellchecker_llm.script import on_f9, on_f10


class TestKeyPress(unittest.TestCase):
    def setUp(self):
        # Set up any necessary mocks or fixtures
        pass

    def test_on_f9(self):
        # Mock any necessary objects or functions
        with MagicMock() as mock_controller:
            # Call the function you want to test
            on_f9(controller=mock_controller)

            # Assert that the correct actions were performed
            mock_controller.pressed.assert_called_once_with("cmd")
            mock_controller.tap.assert_called_once_with("c")


if __name__ == "__main__":
    unittest.main()
