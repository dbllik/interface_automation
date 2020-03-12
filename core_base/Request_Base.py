# coding: utf-8


class RequestBase:

    def __init__(self, filepath):
        self.__domain_name__ = filepath["domain_name"]
        self.__api_name__ = filepath["api_name"]
        self.__cases__ = filepath["cases"]
        self.__method__ = filepath["method"]
        self.__headers__ = filepath["headers"]
        self.__res_url__ = self.__domain_name__ + self.__api_name__

    @property
    def domain_name(self):
        return self.__domain_name__

    @domain_name.setter
    def domain_name(self,domain):
        self.__domain_name__ = domain

    @property
    def api_name(self):
        return self.__api_name__

    @api_name.setter
    def api_name(self,api):
        self.__api_name__ = api

    @property
    def res_url(self):
        return self.__res_url__

    @res_url.setter
    def res_url(self, res_url):
        self.__res_url__ = res_url

    @property
    def params(self):
        return self.__params__

    @params.setter
    def params(self,parms):
        self.__params__ = parms


    @property
    def body(self):
        return self.__body__

    @body.setter
    def body(self,body):
        self.__body__ = body

    @property
    def headers(self):
        return self.__headers__

    @headers.setter
    def headers(self,headers):
        self.__headers__ = headers

    @property
    def method(self):
        return self.__method__

    @method.setter
    def method(self,method):
        self.__method__ = method

    @property
    def cases(self):
        return self.__cases__

    @cases.setter
    def cases(self,cases):
        self.__cases__  = cases

class CaseBase:

    def __init__(self,cases):
        self.cases = cases
        self.comment = cases["comment"]
        self.login = cases["login"]
        self.params = cases["params"]
        self.data = cases["data"]
        self.reponse = cases["respons"]
        self.response_type = cases["response_type"]



