from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

from locators import Strona_Logowania_Lokatory

class StronaLogowania:

    def __init__(self, driver):
        self.driver=driver

    def refresh(self):
        self.driver.refresh()

    def zweryfikuj_strone(self, info, infoA):
        naglowek=self.driver.find_element(*Strona_Logowania_Lokatory.pole_naglowek)
        if naglowek.is_displayed():
            naglowek=naglowek.text.strip()
        assert (naglowek==info or naglowek==infoA)

    def wpisz_uzytkowik(self, uzytkownik):
        WebDriverWait(self.driver,50).until(EC.presence_of_element_located(Strona_Logowania_Lokatory.input_uzytkownik)).send_keys(uzytkownik)

    def wpisz_haslo(self, haslo):
        WebDriverWait(self.driver,50).until(EC.presence_of_element_located(Strona_Logowania_Lokatory.input_haslo)).send_keys(haslo)

    def kliknij_zaloguj(self):
        WebDriverWait(self.driver,50).until(EC.presence_of_element_located(Strona_Logowania_Lokatory.btn_zaloguj)).click()

    def kliknij_powrot(self):
        WebDriverWait(self.driver,50).until(EC.presence_of_element_located(Strona_Logowania_Lokatory.btn_powrot)).click()

    def sprawdz_zle_zalogowanie(self, error, errorA):
        WebDriverWait(self.driver,50).until(EC.presence_of_element_located(Strona_Logowania_Lokatory.pole_error))
        error_info=self.driver.find_element(*Strona_Logowania_Lokatory.pole_error)
        if error_info.is_displayed():
            error_info=error_info.text.strip()
        assert (error_info==error or error_info==errorA)
