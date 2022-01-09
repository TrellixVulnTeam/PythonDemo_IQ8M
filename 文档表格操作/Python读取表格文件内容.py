import xlrd


# 获取表格数据
def get_excel_data(filename):
    # 打开excel文件
    ExcelData = xlrd.open_workbook(filename)
    # 获取表格里面的第一个表格(下方表框)
    # table = ExcelData.sheet_by_name('login')
    table = ExcelData.sheet_by_index(0)
    nrows = table.nrows  # 获取当前表格行数
    case_data = []
    for n in range(nrows):
        if n > 0:
            # 当前行的数据
            colnames = table.row_values(n)
            # print(colnames[-1])
            int_data = int(colnames[-1])
            case_data.append(colnames[1:-1])
            case_data[-1].append(int_data)

    print(type(case_data))
    return case_data


if __name__ == '__main__':
    # 目录填写自己真是表格地址
    ExcelData = get_excel_data("./Tpshop_login.xls")
    for n in ExcelData:
        # 遍历列表
        print(n)
