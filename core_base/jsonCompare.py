# coding: utf-8


class JsonCompare:
    """
        递归对比两个JSON ，并返回对比结果

    """

    def __init__(self):
        self.result = {"STATUS":True}
        self.key_path = []
        self.error_message = []
        self.pass_message = []

    def json_compare(self,source_js,targ_js):
       if isinstance(source_js,dict):
            for key, value in source_js.items():
                if key not in targ_js.keys():
                    self.error_message.append(str(key) + ":不存在结果集")
                    continue
                targ_value = targ_js[key]
                if isinstance(value,list):
                    self.compare_list(key,value,targ_value)
                self.compare_value(key, value, targ_value)
       else:
           self.error_message.append("JSON 格式错误，请传入正确的JSON数据：" + source_js)


    def get_result(self):
        if self.error_message is not None and len(self.error_message) > 0 : self.result["STATUS"] = False
        self.result["ERROR"] = self.error_message
        self.result["PASS"] = self.pass_message
        return self.result

    def compare_value(self,key,expect_value,actual_value):
        if expect_value == actual_value:
            self.pass_message.append(key + "：--对比结果一致: " + str(expect_value))
        else:
            self.error_message.append(key + "：--对比结果不一致， 期望值：" + str(expect_value) + ",  实际值：" + str(actual_value))

    def compare_list(self,key,expect_value,actual_value):
        if actual_value is None or len(actual_value) < 1:
            self.error_message.append(str(key) + ":是空集合")
            return
        targ_len = len(actual_value)
        expect_len = len(expect_value)
        if targ_len != expect_len:
            self.error_message.append(str(key) + ":结果集返回的数据个数不一致")
            return
        for index in range(0, expect_len):
            if isinstance(expect_value[index], dict):
                self.json_compare(expect_value[index], actual_value[index])
            else:
                self.compare_value(key, expect_value[index], actual_value[index])

