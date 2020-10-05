import unittest
import sys
sys.path.append("C:\\Users\\Stevens User\\Documents\\GitHub\\Team-4-Code\\seeds")
sys.path.append("C:\\Users\\Stevens User\\Documents\\GitHub\\Team-4-Code\\GMiguel")
sys.path.append("c:\\Users\\Stevens User\\Documents\\GitHub\\Team-4-Code\\src")
import Project02
import user03

class TestUser03(unittest.TestCase):
    #one death is incorrect
    def test1(self):
        s = "The following have deaths before birth which is incorrect: ANGEL Florene "
        self.assertEquals(s, user03.user03("seeds/test8.ged"))

    #no deaths before births
    def test2(self):
        s = ""
        self.assertEquals(s, user03.user03("seeds/test7.ged"))
    #2 deaths before births
    def test3(self):
        s = "The following have deaths before birth which is incorrect: ANGEL Florene RAYMOND MIGUEL "
        self.assertEquals(s, user03.user03("seeds/test9.ged"))
    
    #no deaths before births
    def test4(self):
        s = ""
        self.assertEquals(s, user03.user03("seeds/test4.ged"))
    
    #no deaths before births
    def test5(self):
        s = ""
        self.assertEquals(s, user03.user03("seeds/test6.ged"))

if __name__ == '__main__':
    unittest.main()

