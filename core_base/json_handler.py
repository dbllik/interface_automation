# coding: utf-8

import json

"""
加载JSON 文件
"""

def loadJSONFile(filepath):
    if filepath is None:
        return
    try:
        with open(filepath,'r',encoding='utf-8') as f:
         res = f.read()
         d = json.loads(res)
         return d
    except Exception as e:
        print(filepath)
        raise e