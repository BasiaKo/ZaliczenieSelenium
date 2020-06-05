import unittest

import HtmlTestRunner

from test_glowna import GlownaTest

class TestSuite(unittest.TestSuite):
    def suite(self):
        suite=unittest.TestSuite()
        suite.addTest(GlownaTest('test_zaladowanie_strony'))

        return suite

if __name__=="__main__":
  unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))
