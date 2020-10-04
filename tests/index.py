'''
This run the entire testing suite
'''
import unittest
import os
# import all test cases properly as class
from us01_test import us01_test
from us07_test import us07_test
from us24_test import us24_test
from us25_test import us25_test
from us41_test import us41_test
from us42_test import us42_test

# add tests to testing "suite" (lol I couldn't get the actually suite working so I leave this for now)
testsuite = [
  us01_test(),
    us24_test(),
    us25_test(),
    us41_test(),
    us42_test()
]

# this doesn't work 100% how I'd like yet but it should check if each test passed
for t in testsuite:
    if t:
        print(t, "passed")
    else:
        print(t, "failed")

# show total tests that have been run
unittest.main()
