from selenium.webdriver.common.by import By

class Strona_Glowna_Lokatory:
  input_miasto=(By.XPATH, "//input[@id='searchAdresu']")
  input_lek=(By.XPATH, "//input[@id='search']")
  btn_szukajAdresu=(By.XPATH, "//button[@id='showAdresy']")
  btn_szukajLeku=(By.XPATH, "//button[@id='showLeki']")
  btn_menu=(By.XPATH, "//button[@id='menuToggler']")
  btn_zaloguj=(By.XPATH, "//div[@class='box t-a:c']/a[@class='b:pri']")
  pole_uzytkownik=(By.XPATH, "//div[@class='logged-in']/p")


class Strona_Logowania_Lokatory:
  input_uzytkownik=(By.XPATH, "//input[@id='josso_username']")
  input_haslo=(By.XPATH, "//input[@id='josso_password']")
  btn_zaloguj=(By.XPATH, "//div[@class='b-b']/input")
  btn_powrot=(By.XPATH, "//div[@class='b-b']/a")
  pole_error=(By.XPATH,"//div[@class='error']")
  pole_naglowek=(By.XPATH,"//div/h1")

class Strona_Zapytaj_Lokatory:
  pole_miasto=(By.XPATH, "//input[@id='searchAdresu']")

class Strona_Ulotka_Lokatory:
  pole_miasto=(By.XPATH, "//input[@id='searchAdresu']")
