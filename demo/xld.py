import xlrd
xld_url = r'C:\Users\28235\Desktop\11\自动化.xlsx'
xld1 = xlrd.open_workbook(xld_url)


def login():
    sheet_name = xld1.sheet_by_name('登录')
    workbook = sheet_name.cell_value(1, 6)
    return workbook


def driver():
    sheet_name = xld1.sheet_by_name('司机添加')
    workbook = sheet_name.cell_value(1, 6)
    return workbook


print(driver())