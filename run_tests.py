from unittest import TextTestRunner, TestSuite, makeSuite

from ctci.tests.test_ch1 import TestChapter1
from ctci.tests.test_ch2 import TestChapter2

if __name__ == '__main__':
    suite = TestSuite()
    suite.addTest(makeSuite(TestChapter1))
    suite.addTest(makeSuite(TestChapter2))

    runner = TextTestRunner()
    runner.run(suite)
