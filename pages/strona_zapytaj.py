from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

from locators import Strona_Zapytaj_Lokatory

class StronaZapytaj:

    def __init__(self, driver):
        self.driver=driver

    def refresh(self):
        self.driver.refresh()

    def zweryfikuj_strone(self):
        self.driver.implicitly_wait(50)
        title="Ktomalek - Zapytaj farmaceutę"
        assert title==self.driver.title

    def wpisz_pytanie(self, pytanie):
        WebDriverWait(self.driver,50).until(EC.presence_of_element_located(Strona_Zapytaj_Lokatory.input_pytanie)).send_keys(pytanie)

    def kliknij_wyslij(self):
        WebDriverWait(self.driver,50).until(EC.element_to_be_clickable(Strona_Zapytaj_Lokatory.btn_wyslij)).click()

    def wyslij_pytanie(self):
        WebDriverWait(self.driver,50).until(EC.element_to_be_clickable(Strona_Zapytaj_Lokatory.btn_wyslij_pytanie)).click()

    def sprawdz_walidacja_dlugosci(self, error_info):
        error=self.driver.find_element(*Strona_Zapytaj_Lokatory.pole_walidacja_dlugosci)
        if error.is_displayed():
            error=error.text.strip()

        assert error==error_info

    def sprawdz_walidacja_zgoda(self, error_info):
        error=self.driver.find_element(*Strona_Zapytaj_Lokatory.pole_walidacja_zgoda)
        if error.is_displayed():
            error=error.text.strip()

        assert error==error_info
