from selenium.webdriver.common.by import By

class Strona_Glowna_Lokatory:
  input_miasto=(By.XPATH, "//input[@id='searchAdresu']")
  input_lek=(By.XPATH, "//input[@id='search']")
  btn_szukajAdresu=(By.XPATH, "//button[@id='showAdresy']")
  btn_szukajLeku=(By.XPATH, "//button[@id='showLeki']")
  btn_menu=(By.XPATH, "//button[@id='menuToggler']/span")
  btn_zaloguj=(By.XPATH, "//div[@class='box t-a:c']/a[@class='b:pri']")
  pole_uzytkownik=(By.XPATH, "//div[@class='logged-in']/p")
  btn_zapytaj_menu=(By.XPATH, "//div[@class='mg-12 pg-6 tg-3 dg-3 t-a:c'][4]/a")
  btn_zapytaj_boczne=(By.XPATH, "//div[@class='sidebar-qanda']/a")
  btn_zapytaj_stopka=(By.XPATH, "//div[@class='mg-5 mp-1 pg-3 dg-2']/p/a[2]")

class Strona_Logowania_Lokatory:
  input_uzytkownik=(By.XPATH, "//input[@id='josso_username']")
  input_haslo=(By.XPATH, "//input[@id='josso_password']")
  btn_zaloguj=(By.XPATH, "//div[@class='b-b']/input")
  btn_powrot=(By.XPATH, "//div[@class='b-b']/a")
  pole_error=(By.XPATH,"//div[@class='error']")
  pole_naglowek=(By.XPATH,"//div/h1")

class Strona_Zapytaj_Lokatory:
  pole_miasto=(By.XPATH, "//input[@id='searchAdresu']")
