import unittest
import siblingsShouldNotMarry

class TestSiblingsShouldNotMarry(unittest.TestCase):

    '''gedcom file with one sibling marriage'''
    def test1(self):
        s = "The following individuals are marrying their siblings, which is not allowed: Sam Smith, Alexa Smith"
        self.assertEqual(s, siblingsShouldNotMarry.siblingsShouldNotMarry("testFiles/test1.ged"))

    '''gedcom file with three sibling marriages'''
    def test2(self):
        s = "The following individuals are marrying their siblings, which is not allowed: Claire Smith, Rachel Smith, Rick Smith, Cody Smith, James Smith, Jen Smith"
        self.assertEqual(s, siblingsShouldNotMarry.siblingsShouldNotMarry("testFiles/test2.ged"))

    '''gedcom file with no sibling marriages'''
    def test3(self):
        self.assertTrue(siblingsShouldNotMarry.siblingsShouldNotMarry("testFiles/test3.ged"))

    '''larger gedcom file with no sibling marriages'''
    def test4(self):
        self.assertTrue(siblingsShouldNotMarry.siblingsShouldNotMarry("testFiles/test4.ged"))

    '''gedcom file with no sibling marriages, 
        but an individual is married to someone with the same name as their sibling '''
    def test5(self):
        self.assertTrue(siblingsShouldNotMarry.siblingsShouldNotMarry("testFiles/test5.ged"))


if __name__ == '__main__':
    unittest.main()