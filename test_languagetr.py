import unittest
from . import languagetr #import en2fr, fr2en
class Testen2fr(unittest.TestCase):
    def test1(self):
        self.assertEqual(languagetr.en2fr(),"Bonjour")
class Testfr2en(unittest.TestCase):
    def test1(self):
        self.assertEqual(languagetr.fr2en(),"hello")
#unittest.main()