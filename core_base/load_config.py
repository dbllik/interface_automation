# coding: utf-8
import configparser

"""
加载配置文件
"""

conf = configparser.ConfigParser()


def loadconfig_ini(filepath="../config/base.ini"):
    conf.read(filenames=filepath)
    return conf
