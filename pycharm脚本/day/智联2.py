#/usr/bin/python
#-*-coding:utf-8-*-
import re,requests,xlwt,xlrd,pymysql
class A(object):
    def __init__(self):
        self.d = xlwt.Workbook()
        self.a = self.d.add_sheet("智联")

    def url(self):
        s1 = []
        res = requests.get(r'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=763&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95&kt=3&_v=0.42261335&x-zp-page-request-id=2604780486c34292a8930b69d90affab-1562659418558-623397&x-zp-client-id=47e79f53-8563-4c28-a02d-2f6c9af44ef0')
        html = res.content.decode('utf-8')
        # print(html )

        a = re.compile('"jobName":"(.*?)"',re.S)
        m = re.findall(a, html)

        a1 = re.compile('"company":{"name":"(.*?)"',re.S)
        m1 = re.findall(a1, html)
        a2 = re.compile('salary":"(.*?)"',re.S)
        m2 = re.findall(a2,html)
        a3 = re.compile('"eduLevel":{"name":"(.*?)"}',re.S)
        m3 = re.findall(a3,html)

        for i in range(len(m)):
            self.a.write(i,0,m[i])
        for w in range(len(m1)):
            self.a.write(w,1,m1[w])
        for w1 in range(len(m2)):
            self.a.write(w1, 2, m2[w1])
        for w2 in range(len(m3)):
            self.a.write(w2, 3, m3[w2])
        self.d.save("智联.xlsx")
    def get(self):
        connect = pymysql.connect(
            host='127.0.0.1',
            user='root',
            port=3306,
            password='123456',
            charset='utf8',
            database = '111'
        )
        cu = connect.cursor()
        # sql1='create table job(`工作名称` varchar(255),`公司` varchar (255),`薪资` varchar (255),`学历` varchar(255))'
        # cu.execute(sql1)
        m1 = xlrd.open_workbook(filename="智联.xlsx")
        sheet= m1.sheet_by_name('智联')
        sum = sheet.nrows
        for i in range(sum):
            m3 = sheet.row_values(i)
            m4 = tuple(m3)
            sq2 = f'insert into job values {m4}'
            cu.execute(sq2)
        cu.close()
        connect.commit()
        connect.close()
s1=A()
# s1.url()
s1.get()