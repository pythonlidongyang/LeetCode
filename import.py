#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/11/26 15:05
# @Author : Dongyang Li
# @File : import.py
'''
excel表格转HTML 表格格式
'''
import xlrd


def update_acmg():
    import_excel = xlrd.open_workbook("F:/Desktop/a.xlsx")  # 得到Excel文件的book对象，实例化对象
    sheet = import_excel.sheet_by_index(0)  # 通过sheet索引获得sheet对象->sheet1
    rows = sheet.nrows  # 获取行总数
    cols = sheet.ncols  # 获取列总数
    print(rows, cols)
    s = ''
    s += '<table>'
    for i in range(1, rows):  # 由于表格有标题，索引从1开始
        s += '<tr>'
        for j in range(0, cols):
            s += '<td>' + sheet.cell_value(i, j) + '</td>'
        s += '</tr>'
    s += '</table>'
    result = open('result.html', 'w', encoding='UTF-8')
    result.write(s)
    print('格式转换成功，请查看附件')


update_acmg()
