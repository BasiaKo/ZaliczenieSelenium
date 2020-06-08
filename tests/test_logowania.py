import unittest

from test_base import BaseTestLogowania, BaseTestGlowna
from pages.strona_glowna import StronaGlowna
from pages.strona_logowania import StronaLogowania

class PrzejscieDoLogowania(BaseTestGlowna):

  def test_strony_logowania(self):
    hp=StronaGlowna(self.driver)
    hp.kliknij_menu()
    hp.kliknij_zaloguj()

    lp=StronaLogowania(self.driver)
    lp.zweryfikuj_strone("Zaloguj się")

class LogowanieZle(BaseTestLogowania):
  def test_zlego_logowania(self):
    uzytkownik="01Barbara"
    haslo="cos"
    error="Podano nieprawidłowe dane dostępowe"

    lp=StronaLogowania(self.driver)
    lp.wpisz_uzytkowik(uzytkownik)
    lp.wpisz_haslo(haslo)
    lp.kliknij_zaloguj()
    lp.sprawdz_zle_zalogowanie(error)

class LogowaniePoprawne(BaseTestLogowania):
  def test_poprawnego_logowania(self):
    uzytkownik="01Barbara"
    haslo="P@ssw0rd"

    lp=StronaLogowania(self.driver)
    lp.wpisz_uzytkowik(uzytkownik)
    lp.wpisz_haslo(haslo)
    lp.kliknij_zaloguj()

    hp=StronaGlowna(self.driver)
    hp.kliknij_menu()
    hp.sprawdz_poprawne_zalogowanie(uzytkownik)

if __name__=="__main__":
  unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))
