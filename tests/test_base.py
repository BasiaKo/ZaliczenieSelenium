import unittest

from selenium import webdriver

class BaseTestGlowna(unittest.TestCase):

  def setUp(self):
    self.driver=webdriver.Firefox()
    self.driver.get("https://ktomalek.pl")
    self.driver.maximize_window()
    self.driver.implicitly_wait(30)

  def tearDown(self):
    self.driver.quit()
