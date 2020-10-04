'''
This run the entire testing suite
'''
import unittest
#import all test cases properly as class
from us41_test import us41_test 
from us42_test import us42_test 

#add tests to testing "suite" (lol I couldn't get the actually suite working so I leave this for now)
testsuite=[us41_test(), us42_test()]

#this doesn't work 100% how I'd like yet but it should check if each test passed
for t in testsuite:
    if t:
        print(t,"passed")
    else:
        print(t,"failed")

#show total tests that have been run
unittest.main()
