# coding: utf-8
from core_base import Result_Base as rb


class ResultHandler:

    def __init__(self,result):
        self.result = result


    def print_result(self):

        for key,value in self.result:
            case = value.case
            status = value.result






