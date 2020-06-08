import unittest
import HtmlTestRunner

from test_base import BaseTestGlowna#, BaseTestZapytaj
from pages.strona_zapytaj import StronaZapytaj
from pages.strona_glowna import StronaGlowna

class PrzejscieDoZapytaj(BaseTestGlowna):

  def test_strony_zapytaj_stopka(self):
    hp=StronaGlowna(self.driver)
    hp.kliknij_zapytaj_stopka()

    zp=StronaZapytaj(self.driver)
    zp.zweryfikuj_strone()

  def test_strony_zapytaj_menu(self):
    hp=StronaGlowna(self.driver)
    hp.kliknij_zapytaj_menu()

    zp=StronaZapytaj(self.driver)
    zp.zweryfikuj_strone()

  def test_strony_zapytaj_boczne(self):
    hp=StronaGlowna(self.driver)
    hp.kliknij_zapytaj_boczne()

    zp=StronaZapytaj(self.driver)
    zp.zweryfikuj_strone()


if __name__=="__main__":
  unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))
