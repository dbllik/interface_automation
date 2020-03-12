# coding: utf-8
from core_base import load_config

class TestCasesConfigBase:

    def __init__(self):
        config_base = load_config.loadconfig_ini("../config/test_cases.ini")
        self.remove_tests = config_base["DIR"]["remove_tests"].split(";")
        self.load_type = config_base["DIR"]["load_type"]
        self.only_test = config_base["DIR"]["only_tests"].split(";")
        self.root = config_base["DIR"]["root"]
