import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

from locators import Strona_Glowna_Lokatory

class StronaGlowna:

    def __init__(self, driver):
        self.driver=driver

    def refresh(self):
        self.driver.refresh()

    def kliknij_menu(self):
        time.sleep(10)
        WebDriverWait(self.driver,50).until(EC.element_to_be_clickable(Strona_Glowna_Lokatory.btn_menu)).click()

    def kliknij_zaloguj(self):
        WebDriverWait(self.driver,50).until(EC.element_to_be_clickable(Strona_Glowna_Lokatory.btn_zaloguj)).click()

    def kliknij_zapytaj_stopka(self):
        time.sleep(10)
        WebDriverWait(self.driver,50).until(EC.element_to_be_clickable(Strona_Glowna_Lokatory.btn_zapytaj_stopka)).click()

    def kliknij_zapytaj_menu(self):
        time.sleep(10)
        WebDriverWait(self.driver,50).until(EC.element_to_be_clickable(Strona_Glowna_Lokatory.btn_zapytaj_menu)).click()

    def kliknij_zapytaj_boczne(self):
        time.sleep(10)
        WebDriverWait(self.driver,50).until(EC.element_to_be_clickable(Strona_Glowna_Lokatory.btn_zapytaj_boczne)).click()

    def sprawdz_poprawne_zalogowanie(self, uzytkownik):
        zalogowany=self.driver.find_element(*Strona_Glowna_Lokatory.pole_uzytkownik)
        if zalogowany.is_displayed():
            zalogowany=zalogowany.text.strip()

        assert zalogowany==uzytkownik
