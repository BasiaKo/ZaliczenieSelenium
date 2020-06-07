from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdrive import ActionChains

from locators import Strona_Ulotka_Lokatory

class StronaUlotka:

    def __init__(self, driver):
        self.driver=driver

    def refresh(self):
        self.driver.refresh()

    def click_menu(self):
        WebDriverWait(self.driver,50).until(EC.presence_of_element_located(btn_menu)).click()
