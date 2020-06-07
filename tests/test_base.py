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

class BaseTestLogowania(unittest.TestCase):

  def setUp(self):
    self.driver=webdriver.Firefox()
    self.driver.get("https://www.osoz.pl/josso/signon/login.do?josso_back_to=http://ktomalek.pl/leon-www/rezerwacjeLekow/KLEK/logowaniePost?bp=eyJhZHJlcyI6Ii9sZW9uLXd3dy9yZXplcndhY2plTGVrb3cvS0xFSy9nZHppZUt1cGllTGVraSJ9&josso_partnerapp_id=leon-www")
    self.driver.maximize_window()
    self.driver.implicitly_wait(30)

  def tearDown(self):
    self.driver.quit()

class BaseTestZapytaj(unittest.TestCase):

  def setUp(self):
    self.driver=webdriver.Firefox()
    self.driver.get("https://ktomalek.pl/pytania-i-odpowiedzi")
    self.driver.maximize_window()
    self.driver.implicitly_wait(30)

  def tearDown(self):
    self.driver.quit()

class BaseTestUlotka(unittest.TestCase):

  def setUp(self):
    self.driver=webdriver.Firefox()
    self.driver.get("https://ktomalek.pl/l/lek/szukaj")
    self.driver.maximize_window()
    self.driver.implicitly_wait(30)

  def tearDown(self):
    self.driver.quit()
