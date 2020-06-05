import unittest

import HtmlTestRunner

from test_base import BaseTestGlowna

class GlownaTest(BaseTestGlowna):

  def test_zaladowanie_strony(self):
    assert "KtoMaLek" in self.driver.title


if __name__=="__main__":
  unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))
