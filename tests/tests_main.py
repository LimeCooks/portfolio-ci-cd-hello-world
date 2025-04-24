import unittest
from app.main import get_message

class TestMain(unittest.TestCase):
    def test_get_message(self):
        self.assertEqual(get_message(), "Hello, Secure World!")
        
if __name__ == "__main__":
    unittest.main()