#/usr/bin/python
#-*-coding:utf-8-*-
print('这个abc里的代码')

"""
if __name__ == '__main__':
__name__  自动获取当前文件的名字
'__main__'  代表当前文件的名字
"""

#python的程序入口，只能在当前文件下执行  if __name__ == '__main__':  下的代码
#离开这个文件  if __name__ == '__main__':  条件就不成立了
if __name__ == '__main__':
    print('这是if语句下的代码')