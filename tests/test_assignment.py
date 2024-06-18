import unittest

class TestHelloWorld(unittest.TestCase):

    def test_hello_world(self):
        from main import hello_world
        self.assertEqual(hello_world(), "Hello, World!")

if __name__ == '__main__':
    unittest.main()
