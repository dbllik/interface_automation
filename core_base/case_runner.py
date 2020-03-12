# coding: utf-8


from core_base import case_handler
from core_base import url_handler
from core_base import Request_Base
from core_base import jsonCompare
from core_base import Result_Base
import datetime
import requests

class FileCasesRunner:
    """
        执行用例的类

    """
    def __init__(self,tests_file):
        self.tests_file = tests_file
        self.ca_handler = case_handler
        self.url_hand = url_handler
        self.all_test = []
        self.results = {"total_count":0,"start_time":0,"result":{},"end_time":0,"excute_status":"PASS"}
        self.total_count = 0
        self.excute_status = "PASS"



    def run(self):
        start_time = datetime.datetime.now()
        self.get_all_tests()
        case_session = self.ca_handler.get_login_session()
        tmp_result = {}
        for test in self.all_test:
            test_url = test.res_url
            test_method = test.method
            test_cases = test.cases
            test_heard = test.headers
            test_result = []
            test_result.clear()
            for case in test_cases:
                compare = jsonCompare.JsonCompare()
                case_base = Request_Base.CaseBase(case)
                expect_respons = case_handler.get_json_from_file(case_base.reponse)
                if case_base.login is not True:
                   case_session = requests
                if test_method == "POST":
                    actual_reponse = case_session.post(url=test_url,data=case_base.data,headers=test_heard)
                else:
                    actual_reponse = case_session.get(url=test_url,params=case_base.params,headers=test_heard)
                response_status = actual_reponse.status_code
                if response_status != 200:
                    compare.result = {"STATUS":False,"ERROR":"请求返回的状态码不为200, 而是：" + str(response_status),"PASS":""}
                else:
                    compare.json_compare(expect_respons, actual_reponse.json())
                result = compare.get_result()
                if result["STATUS"] is not True:
                    self.results["excute_status"] = "FAIL"
                result_base = Result_Base.ResultBase(case,result)
                test_result.append(result_base)
                self.total_count += 1
            tmp_result[test.api_name] = test_result
        end_time = datetime.datetime.now()
        self.results["total_count"] = self.total_count
        self.results["start_time"] = start_time
        self.results["end_time"] = end_time
        self.results["result"] = tmp_result
        return self.results

    def get_all_tests(self):
        if self.check_list_is_none(self.tests_file):
            raise Exception("没有用例文件")
        for test in self.tests_file:
            request_base = self.url_hand.CreateUrlHandler(test).reuest_base
            self.all_test.append(request_base)



    def check_list_is_none(self,lis):
        res = False
        if lis is None or len(lis) <= 0:
            res = True
        return res




if __name__ == '__main__':
   fr = FileCasesRunner(["E:/interface_work_file/url_config/KeInsight_main_node_request.json"])
   res =  fr.run()
   print(res)
   for api_name,cases in res["result"].items():
       print(api_name + "用例如下：")
       for cas in cases:
          print(cas.result)
          print(cas.case["comment"])