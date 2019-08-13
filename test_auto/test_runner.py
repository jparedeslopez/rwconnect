import unittest
import xmlrunner


#Test Scenario 1
from test_auto.tests.test1 import TestScenario01


if __name__ == "__main__":
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports',
                                                     outsuffix="Test-IOS"))
