import unittest

import HtmlTestRunner

# from tests.test_glowna import GlownaTest
# import tests.test_logowania as logowanie
from tests.test_logowania import PrzejscieDoLogowania #LogowanieZle, LogowaniePoprawne
from tests.test_zapytaj import PrzejscieDoZapytaj, ZadaniePytaniaWalidacje

class TestSuite(unittest.TestSuite):
    def suite(self):
        suite=unittest.TestSuite()
        # suite.addTest(GlownaTest('test_zaladowanie_strony'))
        # suite.addTest(LogowanieZle('test_zlego_logowania'))
        suite.addTest(PrzejscieDoLogowania('test_strony_logowania'))
        # suite.addTest(LogowaniePoprawne('test_poprawnego_logowania'))
        suite.addTest(PrzejscieDoZapytaj('test_strony_zapytaj_stopka'))
        suite.addTest(PrzejscieDoZapytaj('test_strony_zapytaj_menu'))
        suite.addTest(PrzejscieDoZapytaj('test_strony_zapytaj_boczne'))
        suite.addTest(ZadaniePytaniaWalidacje('test_dlugosci_znakow'))
        suite.addTest(ZadaniePytaniaWalidacje('test_zgody'))

        return suite

if __name__=="__main__":
  unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))
