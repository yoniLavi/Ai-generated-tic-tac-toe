import unittest
import sys

if __name__ == "__main__":
    # Discover and run all tests
    test_suite = unittest.defaultTestLoader.discover(".", pattern="test_*.py")
    result = unittest.TextTestRunner(verbosity=2).run(test_suite)

    # Print a summary of the test results
    print(f"\nTest Summary:")
    print(f"Ran {result.testsRun} tests")
    print(f"Successes: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")

    # Set the exit code based on the test results
    sys.exit(len(result.failures) + len(result.errors))
