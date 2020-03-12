# coding: utf-8


from core_base import test_cases_config_base
import os


class LoadCases:
    """
        根据配置加载用例文件

    """

    def __init__(self):
        self.all_files = []
        self.conf_base = test_cases_config_base.TestCasesConfigBase()

    def get_all_files(self,filepath):
        if filepath is None:
            return []

        all_temp = os.listdir(filepath)
        for f in all_temp:
            chaild = os.path.join('%s/%s' % (filepath, f))
            if os.path.isdir(chaild):
                self.get_all_files(chaild)
            else:
                self.all_files.append(chaild)

    def delete_tests(self,all_test):
        de_case = self.conf_base.remove_tests
        temp_list = []
        if de_case is None or len(de_case) <= 0:
            return

        for at in all_test:
            for de in de_case:
               if de in at:
                   temp_list.append(at)
                   break
        if len(temp_list) > 0:
            for t in temp_list:
                all_test.remove(t)
        return all_test

    def only_tests(self,all_test):
        ol_case = self.conf_base.only_test
        temp_list = []

        if ol_case is None or len(ol_case) <= 0:
            return
        for at in all_test:
            for ol in ol_case:
                if ol in at:
                    temp_list.append(at)
        return temp_list

    def load_cases(self):
        filepath = self.conf_base.root
        load_type = self.conf_base.load_type
        self.get_all_files(filepath)
        all_test = self.all_files
        if load_type == "ONLY":
            all_test = self.only_tests(all_test)
        elif load_type == "REMOVE":
            all_test = self.delete_tests(all_test)
        return all_test








