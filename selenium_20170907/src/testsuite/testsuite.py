# coding: utf-8
import unittest
from firstcase import SearchTest
from secondcase import LoginTest
import HTMLTestRunner


firstcase = unittest.TestLoader().loadTestsFromTestCase(SearchTest)
secondcase = unittest.TestLoader().loadTestsFromTestCase(LoginTest)

test_suite = unittest.TestSuite([firstcase,secondcase])

#unittest.TextTestRunner(verbosity=2).run(test_suite)   普通执行

#输出到HTML
outfile = open('/Users/zhanghui/Documents/TestReport/SeleniumPythonTestSummary.html','w')

runner = HTMLTestRunner.HTMLTestRunner(stream=outfile,title='Test Report',description='Acceptance Tests')

runner.run(test_suite)