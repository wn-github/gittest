#/usr/bin/python
#-*-coding:utf-8-*-

import xlrd

# 操作Excel的xlrd读取Excel文件  xlwt写入数据到Excel文件

# 第一步：打开Excel
# d = xlrd.open_workbook(filename='222.xlsx')

# 第二步：选中一个子表 sheet1 sheet1
# table = d.sheets()[0]
# print(table)
"""
第二种方法
"""
# table = d.sheet_by_index(0)
# print(table)

# 第三步：获取数据

# 获取指定整行数据，必须指定获取的行号
# a = table.row_values(0)
# print(a)

# 获取某一个单元格的值

# 获取一行  --->  返回的是一个列表
# 再通过列表的索引获取到元素   --->   .value  获取到具体的值
# print( table.row(0)[0].value )

# 先获取一列   col（）  --->  返回一个列表
# 再通过列表的索引获取到元素   --->   .value  获取到具体的值
# print( table.col(0)[0].value )

# 通过行、列索引获取具体单元格的值
# print( table.cell( 0 , 2 ).value )

# 获取行数、列数
"""
nrows：获取行数
ncols：获取列数
"""

# print(table.nrows)
# print(table.ncols)

# 如何获取所有行数据
# h = table.nrows
# for i in  range(h):
#     hang = table.row_values(i)
#     print(hang)


# 获取所有列数据
# l = table.ncols
# for i in  range(l):
#     lie = table.col_values(i)
#     print(lie)

# sheet_names():找出文件中所有表的名字
# print(d.sheet_names())



"""
定一个类：
1.可以打开不同的Excel文件
2.按照行读取任意行数据  2 ~ 3
3.读取指定单元格的数据  0 ，4
4.按照列读取任意列数据  2 ~ 3
5.指定读取某个表格的数据
"""

# class Excel(object):
#
#     def __init__(self, name, n):
#         # 对象属性
#         self.name = name  # Excel文件名
#         self.n = n  # 表格
#         # 局部变量
#         # d = xlrd.open_workbook(filename=self.name)
#         self.d= xlrd.open_workbook(filename=self.name)
#         # 打开某一张表
#         self.table = self.d.sheets()[self.n]
#
#     # 读取任意行数据
#     def read_row_data(self):
#         a = int(input("输入查询的第一个行号"))
#         b = int(input("输入查询的第二个行号"))
#         if a > b:
#             if a > self.table.nrows:
#                 print("超出查询范围")
#                 return None
#             else:
#                 for i in range(b, a + 1):
#                     print(self.table.row_values(i))
#         else:
#             if b > self.table.nrows:
#                 print("超出查询范围")
#                 return None
#             else:
#                 for i in range(a, b + 1):
#                     print(self.table.row_values(i))
#
#
#     # 读取任意行数据
#     def read_col_data(self):
#         a = int(input("输入查询的第一个列号"))
#         b = int(input("输入查询的第二个列号"))
#         if a > b:
#             if a > self.table.ncols:
#                 print("超出查询范围")
#                 return None
#             else:
#                 for i in range(b, a + 1):
#                     print(self.table.col_values(i))
#         else:
#             if b > self.table.ncols:
#                 print("超出查询范围")
#                 return None
#             else:
#                 for i in range(a, b + 1):
#                     print(self.table.col_values(i))
#
#     # 读取任意单元格
#     def read_cell_data(self):
#         a = int(input("输入要查询的单元格的行号"))
#         b = int(input("输入要查询的单元格的列号"))
#         print(self.table.cell(a, b).value)
#
#     # 定义主函数
#     def main(self):
#         print("1:查询任意列数据"
#               "2:查询任意行数据"
#               "3:查询任意单元格数据"
#               "4:退出")
#         while True:
#             chose = input("输入你的选择")
#             if chose == '1':
#                 self.read_col_data()
#             elif chose == '2':
#                 self.read_row_data()
#             elif chose == '3':
#                 self.read_cell_data()
#             elif chose == '4':
#                 break
#             else:
#                 print("不支持此功能")
#
#
# if __name__ == '__main__':
#     e = Excel('222.xlsx', 0)
#     e.main()


import xlwt

#
# a = [
#     ["序号", "名字", "年龄", "性别"],
#     [1, "张三", 20, "男"],
#     [2, "李四", 19, "男"],
#     [3, "王五", 18, "女"],
#     [4, "赵信", 16, 	"女"]
#     ]
# 第一步：新建一个excel文件
# xlwt.Workbook()
# d = xlwt.Workbook()

# 第二步：新建一个excel表   add_sheet(工作表的名字)表名必填
# table = d.add_sheet('sheet2')

# 第三步：写入数据到excel表中
# 一次写入一个单元格
# write(行号 , 列号 , '写入的数据')

# for i in range(len(a)):
#     for j in range(len(a[i])):
#         table.write(i,j,a[i][j])

# 第四步：保存excel文件
# save('excel文件名')
# d.save('111.xls')




f = open(file='a.txt',mode='r',encoding='utf-8')
g = f.read()
h = []
c = g.replace('(','').replace(';','').replace('\n','').split('),')
for i in c:
    h.append(i.replace("'",'').split(','))
print(h)
# 第一步：新建一个excel文件
xlwt.Workbook()
d = xlwt.Workbook()

# 第二步：新建一个excel表   add_sheet(工作表的名字)表名必填
table = d.add_sheet('sheet1')

# 第三步：写入数据到excel表中
# 一次写入一个单元格
# write(行号 , 列号 , '写入的数据')


# a = ['编号', '公司名', '职位', 'URL', '类别',
#
# '是否上市', '人数','地址','工作经验', '最低学历要求']
for i in range(len(h)):
    for j in range(len(h[i])):
        table.write(i,j,h[i][j])

# 第四步：保存excel文件
# save('excel文件名')
d.save('333.xls')

