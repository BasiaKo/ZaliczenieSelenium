import unittest

import HtmlTestRunner

from tests.test_glowna import GlownaTest
# import tests.test_logowania as logowanie
from tests.test_logowania import LogowanieZle, PrzejscieDoLogowania, LogowaniePoprawne

class TestSuite(unittest.TestSuite):
    def suite(self):
        suite=unittest.TestSuite()
        suite.addTest(GlownaTest('test_zaladowanie_strony'))
        suite.addTest(LogowanieZle('test_zlego_logowania'))
        suite.addTest(PrzejscieDoLogowania('test_strony_logowania'))
        suite.addTest(LogowaniePoprawne('test_poprawnego_logowania'))

        return suite

if __name__=="__main__":
  unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))
