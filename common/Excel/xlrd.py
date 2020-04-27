# coding:utf-8
import xlrd     # 导入excel的库

class xlrd():
    # 打开文件
    workbook = xlrd.open_workbook('E:/huangye/case/common/excel/xlrd_case.xlsx')
    # 获取所有sheet
    # print(workbook.sheet_names())

    # 根据sheet索引或者名称获取sheet内容
    sheet1 = workbook.sheet_by_index(0) # sheet索引从0开始，文档第一格是用例
    sheet2 = workbook.sheet_by_index(1) # 文档第二格是参数
    sheet3 = workbook.sheet_by_index(2)
    sheet4 = workbook.sheet_by_index(3)
    # 打印sheet的名称，行数，列数
    # print(sheet1.name,sheet1.nrows,sheet1.ncols)

    # 获取整行和整列的值(数组)
    rowx = sheet1.row_values(1) # 获取第1行内容
    coly = sheet1.col_values(1) # 获取第2列内容
    # print(rows)
    # print(cols)

    """获取参数"""
    def read_excel(x,y):
        # 获取用例sheet单元格内容
        sheet_value = xlrd.sheet1.cell_value(x,y)
        # 返回方法，使调用这个方法的时候值等于sheet_value
        return sheet_value

    def read_excel_two(x,y):
        # 获取参数sheet的单元格内容
        sheet_value = xlrd.sheet2.cell_value(x,y)
        # 返回方法，使调用这个方法的时候值等于sheet_value
        return sheet_value

    def read_excel_three(x,y):
        # 获取断言sheet的单元格内容
        sheet_value = xlrd.sheet3.cell_value(x,y)
        # 返回方法，使调用这个方法的时候值等于sheet_value
        return sheet_value

    def read_excel_four(x,y):
        # 获取断言sheet的单元格内容
        sheet_value = xlrd.sheet4.cell_value(x,y)
        # 返回方法，使调用这个方法的时候值等于sheet_value
        return sheet_value


