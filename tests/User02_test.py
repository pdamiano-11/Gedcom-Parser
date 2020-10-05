import sys
import unittest
import os
sys.path.append(os.path.abspath('../src'))
sys.path.append(os.path.abspath('../src/seeds'))
sys.path.append("C:\\Users\\Stevens User\\Documents\\GitHub\\Team-4-Code\\GMiguel")
sys.path.append("c:\\Users\\Stevens User\\Documents\\GitHub\\Team-4-Code\\src")
import user02


class Testuser02(unittest.TestCase):
    #all marriages after birth

    def test01(self):
        s = ""
        self.assertEquals(s, user02.user02("seeds/test1.ged"))

    def test02(self):
        s = ""
        self.assertEquals(s, user02.user02("seeds/test2.ged"))

    def test03(self):
        s = ""
        self.assertEquals(s, user02.user02("seeds/test3.ged"))
    def test04(self):
        s = ""
        self.assertEquals(s, user02.user02("seeds/test4.ged"))
    def test05(self):
        s = ""
        self.assertEquals(s, user02.user02("seeds/test5.ged"))

if __name__ == '__main__':
    unittest.main()
