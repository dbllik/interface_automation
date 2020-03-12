# coding: utf-8

from core_base import load_config
from core_base import LoadCases
from core_base import case_runner
from core_base import result_recoder


runn_type = load_config.loadconfig_ini()["DEFAULT"]["runn_type"]

all_cases = LoadCases.LoadCases().load_cases()
if all_cases is None or len(all_cases) <= 0:
    raise Exception("未读取到用例。")

file_runner = case_runner.FileCasesRunner(all_cases)


case_result = file_runner.run()


result_recoder.recode_result_to_excel(case_result)





