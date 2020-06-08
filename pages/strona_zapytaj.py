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
