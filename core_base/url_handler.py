# coding: utf-8

import hashlib
import datetime


from core_base import json_handler as lj
from core_base import Request_Base as rb


class CreateUrlHandler:

    def __init__(self, filepath):
        if filepath is not None:
            self.fileRes = lj.loadJSONFile(filepath)
            self.reuest_base = rb.RequestBase(self.fileRes)
        else:
            raise FileNotFoundError("文件路径为空")














    def assemble_params(self,api_name,params):
        """
            参数组装，赋值
        """
        targ = self.get_target_url(api_name)
        if targ and params is  None:
            Logger.logger.error("读取参数文件或者参数赋值为空")
            return
        for par in list(params):
            targ["params"][par] = params[par]

        return targ["params"]


    def get_target_url(self,target):
        """
        获取目标url
        :param target: 目标api
        :return:
        """
        if target is None:
            Logger.logger.error("target url is None")
        for u in self.fileRes["urls"]:
            if u["api_name"] == target:
                return u
        raise Exception("can not find target url in file")


    def get_response_data(self,api_name,params,domain_name=""):
        """
        通过url 获取数据
        :param domain_name: 域名
        :param api_name: api接口
        :param params: 参数字典
        :return: 返回的是JSON
        """
        fileres = self.assemble_params(api_name, params)
        if self.domain_name is not None:
            url = self.domain_name + api_name
        else:
            url = domain_name + api_name
        res = cs.get_response(url, fileres)
        return res


    def MD5_decode(self,parms,salt = "8c0433e0atc32401110ccfb2aa4f3133",sort=True,include_sign=False):
        """
        获取url的MD5加密字串
        :param parms: 需要加密的参数
        :param salt: 加密盐值
        :param sort: 是否需要对参数排序
        :return: 返回加密字串
        """
        url1 = self.url_to_string(parms,sort,include_sign)
        url2 = url1 + salt
        md = hashlib.md5()
        Logger.logger.info("加密字串：%s"%url2)
        md.update(url2.encode("utf-8"))
        md5_key = md.hexdigest()
        return md5_key

    def get_delta_minutes(self,dminutes):
        """
        获取当前时间延迟分钟数的时间戳
        :param dminutes: 需要延迟的分钟数
        :return: 返回一个整型的时间戳
        """
        return  int((datetime.datetime.now() + datetime.timedelta(minutes=dminutes)).timestamp()*1000)


    def url_to_string(self,params,sort=True,include_sign=False):
        """
        把参数组装成链接字符串
        :param params: 参数字典
        :param sort: 是否排序
        :return:
        """
        keys = params.keys()
        if include_sign is not True and "sign" in params:
           del params["sign"]
        if sort:
            keys = sorted(params)
        url_string = ""
        for key in keys:
            url_string = url_string + key + "=" + str(params[key]) + "&"
        Logger.logger.info("返回url 字串："+url_string[:-1])
        return url_string[:-1]

if __name__ == '__main__':
    print(rb.RequestBase())