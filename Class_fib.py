# -*- coding: utf-8 -*-
# @Time    : 2017-9-21 10:21
# @Author  : zhangqi
# @File    : Class_fib.py
# @Software: PyCharm Community Edition



def fib2(i):
    for j in range(i):
        





def fib(i):
    """
    :param i:int number
    :return: one fibo number
    """
    if i <= 2:
        return i
    else:
        return fib(i-1) + fib(i - 2)



if __name__ == '__main__':
    # 获取用户输入
    nterms = int(input("您要输出几项? "))

    # 检查输入的数字是否正确
    if nterms <= 0:
        print("输入正数")
    else:
        print("斐波那契数列:")
        print(fib(nterms - 1))
        for i in range(nterms):
            print(fib(i))


