from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class StronaGlowna:

    pole_miasto=(By.XPATH, "//input[@id='searchAdresu']")
    pole_lek=(By.XPATH, "//input[@id='search']")
    btn_szukajAdresu=(By.XPATH, "//button[@id='showAdresy']")
    btn_szukajLeku=(By.XPATH, "//button[@id='showLeki']")
    btn_menu=(By.XPATH, "//button[@id='menuToggler']")

    def __init__(self, driver):
        self.driver=driver

    def refresh(self):
        self.driver.refresh()

    def click_menu(self):
        WebDriverWait(self.driver,50).until(EC.presence_of_element_located(btn_menu)).click()
