import os
import unittest
from src.common.HTMLTestRunner_PY3 import HTMLTestRunner


class RunApiTestManager:
    def __init__(self, run_test_case):

        self.report_title = 'Web API 測試報告'
        self.desc = '可以敘述此報告用途是做什麼'
        self.report_file = os.getcwd() + '/report/test_report.html'
        self.run_test_case = run_test_case

    def run_case(self):
        all_case = unittest.defaultTestLoader.discover(os.getcwd() + '/test_cases/', pattern="{0}.py".format(self.run_test_case))
        with open(self.report_file, 'wb') as report:
            """
            先取得基本資訊 名稱、敘述，接著把所有測試用例跑過一輪，儲存到對應的位置。
            """
            runner = HTMLTestRunner(stream=report, title=self.report_title, description=self.desc)
            runner.run(all_case)

if __name__ == '__main__':
    run = RunApiTestManager('web*')
    run.run_case()
