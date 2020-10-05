import unittest
import sys
import os
sys.path.append(os.path.abspath('../src/UserStories')
import us03
sys.path.append(os.path.abspath('../tests/src/seeds'))

class TestUser03(unittest.TestCase):
    #one death is incorrect
    def test1(self):
        s = "The following have deaths before birth which is incorrect: ANGEL Florene "
        self.assertEquals(s, us03.us03("seeds/test8.ged"))

    #no deaths before births
    def test2(self):
        s = ""
        self.assertEquals(s, us03.us03("seeds/test7.ged"))
    #2 deaths before births
    def test3(self):
        s = "The following have deaths before birth which is incorrect: ANGEL Florene RAYMOND MIGUEL "
        self.assertEquals(s, us03.us03("seeds/test9.ged"))
    
    #no deaths before births
    def test4(self):
        s = ""
        self.assertEquals(s, us03.us03("seeds/test4.ged"))
    
    #no deaths before births
    def test5(self):
        s = ""
        self.assertEquals(s, us03.us03("seeds/test6.ged"))

if __name__ == '__main__':
    unittest.main()
