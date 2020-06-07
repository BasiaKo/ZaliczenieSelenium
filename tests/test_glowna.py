import unittest
import HtmlTestRunner

from tests.test_base import BaseTestGlowna
from pages.strona_glowna import StronaGlowna
from locators import Strona_Glowna_Lokatory

class GlownaTest(BaseTestGlowna):

  def test_zaladowanie_strony(self):
    assert "KtoMaLek" in self.driver.title


if __name__=="__main__":
  unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))
