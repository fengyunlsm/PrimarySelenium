#coding=utf-8
import xlrd
from xlutils.copy import copy
import time


class ExcelUtil:
    def __init__(self, excel_path=None, index=None):
        if excel_path == None:
            self.excel_path = "D:\\pyProject\\PrimarySelenium\\config\\casedata.xls"
        else:
            self.excel_path = excel_path
        if index == None:
            index = 0
        else:
            index = index
        
        self.data = xlrd.open_workbook(self.excel_path)
        self.table = self.data.sheets()[index] # 通过索引来获取第一个表格

    def get_data(self):
        """
            读取Excel表格里面的数据，并将其添加到list里面
        """
        result= []
        rows = self.get_lines()
        if rows != None:
            for i in range(rows):
                row_data = self.table.row_values(i)
                result.append(row_data)
            return result
        else:
            return None


    # 获取Excel 行数
    def get_lines(self):
        rows = self.table.nrows
        if rows >= 1:
            return rows
        else:
            return None


    # 获取单元格的数据
    def get_col_value(self, row, col):
        if self.get_lines() > row:
            data = self.table.cell(row, col).value
            return data
        else:
            return None


    # 写入数据
    def write_value(self, row, value):
        read_value = xlrd.open_workbook(self.excel_path)
        write_data = copy(read_value)
        write_data.get_sheet(0).write(row,9,value)
        write_data.save(self.excel_path)
        time.sleep(1)

if __name__ == "__main__":
    ex = ExcelUtil()
    print()
