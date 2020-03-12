# coding: utf-8

from core_base import load_config,url_handler,json_handler
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_login_session():
    """
    获取登录session
    :return: session
    """
    url_file = "../url_config/login.json"
    url_bs = url_handler.CreateUrlHandler(url_file).reuest_base
    data = url_bs.cases[0]["params"]
    s = requests.session()
    res = s.post(url=url_bs.res_url, data=data, verify=False)
    if res.status_code != 200 or res.json()["success"] is not True:
        raise Exception("登录失败！！！")
    return s

def get_request_base(filename=""):
    """
    :param filename: 项目路径下的目录加文件名
    :return: request_base
    """
    requests_base = url_handler.CreateUrlHandler(filename).reuest_base
    return requests_base

def get_json_from_file(filename=""):
    """
    读取JSON文件
    :param filename:
    :return:
    """
    json_res = json_handler.loadJSONFile(filename)
    return json_res
