import unittest
from tests.create_account_test import CreateAccountTest

# Load tests to run
create_account_tests = unittest.TestLoader().loadTestsFromTestCase(CreateAccountTest)

# List of tests to run
tests_to_run = [
    create_account_tests,
    # next
    # ... next test
]

# Create Test Suite - join tests
test_suite = unittest.TestSuite(tests_to_run)

# Run tests
unittest.TextTestRunner().run(test_suite)