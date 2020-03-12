# coding: utf-8

import datetime
import pymysql
import xlwt

"""
    用例执行结果处理

"""


def set_style(name, height, bold=False):
    style = xlwt.XFStyle()   # 初始化样式
    font = xlwt.Font()       # 为样式创建字体
    font.name = name
    font.bold = bold
    font.color_index = 4
    font.height = height
    style.font = font

    return style


def write_data(path,result):
    workbook = xlwt.Workbook(encoding="utf-8")
    data_sheet = workbook.add_sheet("prent")
    total = result["total_count"]
    start_time = result["start_time"].strftime("%Y-%m-%d %H:%M:%S")
    end_time = result["end_time"].strftime("%Y-%m-%d %H:%M:%S")
    status = result["excute_status"]
    data_sheet.write(0,0,"Test Result",set_style('Times New Roman',220,bold=True))
    data_sheet.write(1,0,"开始时间：" + start_time,set_style('Times New Roman',220))
    data_sheet.write(2, 0, "结束时间：" + end_time, set_style('Times New Roman', 220))
    data_sheet.write(3, 0, "用例条数：" + str(total), set_style('Times New Roman', 220))
    data_sheet.write(3, 1, "执行情况：" + str(status), set_style('Times New Roman', 220,bold=True))
    data_sheet.write(4, 0, "详细用例执行情况", set_style('Times New Roman', 220, bold=True))
    case_title = ["api_name","用例名称","pass_message","error_message","status"]

    for ti in range(len(case_title)):
        data_sheet.write(5, ti, case_title[ti], set_style('Times New Roman', 220, bold=True))

    details_res = result["result"]
    index_row = 6
    for api_name, case_result in details_res.items():
        api_name = pymysql.escape_string(api_name)
        data_sheet.write(index_row, 0,api_name, set_style('Times New Roman', 220))
        index_row = index_row + 1
        for cas in case_result:
            case_base = cas.case
            excu_result = cas.result
            case_name = pymysql.escape_string(case_base["comment"])
            excu_status = excu_result["STATUS"]
            error_message = pymysql.escape_string(str(excu_result["ERROR"]))
            pass_message = pymysql.escape_string(str(excu_result["PASS"]))

            data_sheet.write(index_row, 1, case_name, set_style('Times New Roman', 220))
            data_sheet.write(index_row, 2, pass_message, set_style('Times New Roman', 220))
            data_sheet.write(index_row, 3, error_message, set_style('Times New Roman', 220))
            if excu_status:
                data_sheet.write(index_row, 4, "PASS", set_style('Times New Roman', 220))
            else:
                data_sheet.write(index_row, 4, "FAIL", set_style('Times New Roman', 220))
            index_row = index_row + 1
    workbook.save(path)


def recode_result_to_excel(result):
    time_str = datetime.datetime.now().strftime("%Y-%m-%d-%H%M%S")
    path = "../reports/report_"+time_str+".xls"
    write_data(path,result)

