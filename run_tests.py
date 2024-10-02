import unittest

if __name__ == '__main__':
    # Discover and run all tests
    test_suite = unittest.defaultTestLoader.discover('.', pattern='test_*.py')
    unittest.TextTestRunner(verbosity=2).run(test_suite)
