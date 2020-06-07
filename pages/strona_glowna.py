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
        WebDriverWait(self.driver,50).until(EC.presence_of_element_located(Strona_Glowna_Lokatory.btn_menu)).click()

    def kliknij_zaloguj(self):
        WebDriverWait(self.driver,50).until(EC.presence_of_element_located(Strona_Glowna_Lokatory.btn_zaloguj)).click()

    def sprawdz_poprawne_zalogowanie(self, uzytkownik):
        kliknij_menu()
        zalogowany=self.driver.find_element(*Strona_Glowna_Lokatory.pole_uzytkownik)
        if zalogowany.is_displayed():
            zalogowany=zalogowany.text.strip()

        assert zalogowany==uzytkownik
