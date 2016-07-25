# coding=utf-8
'''
Created on 2016-7-21

@author: Dell
'''
from test.test_support import sortdict
from audioop import reverse


def calc(x, y=0):
        list1 = ['zhangsan', 'lisi', 'wangwu']
        if(x > 0):
            list1.append('last')
        else:
            list1.pop(0)
        list1.insert(1, 'second')
        return list1

def calc2():
    t = ('hunan', ['f1', 'f2'], 'zhanjiajie')
    if t.__contains__('hunan'):
        return 'ok' + t[1][1]
    else:
        return 'no'
    return t

def calc3(x):
    if x:
        print('false')
    else:
        print(x)

def calc4():
    list3 = [1, 3, 5, 7, 9]
    list3[1:3] = [2, 4, 6, 8]
    return list3

def calc5():
    prefix = 'hello'
    for var in {1, 2, 3}:
        print(var)

def calc6(n):
    if (n > 100 and n < 500) or (n > 1000 and n < 5000):
        print('111111')
    else:
        print('222222')

def calc7():
    a = [22, 11, 2, 445, 23, 22, 22, 555, 1, 3, 4, 99]
#     a.sort(cmp=None, key=None, reverse=True)
#     print sorted(a,reverse=True)
    for x in range(len(a)):
#         print(len(a) - x - 1)
        for y in range((len(a) - x - 1)):
            if a[y] > a[y + 1]:
                a[y], a[y + 1] = a[y + 1], a[y]
    return a
                
if __name__ == '__main__':
    print(calc(4))
    print(calc(-4))
    print(calc2())
    l = []
    print(0)
    print(range(10))
    print(calc4())
    print(calc5())
    calc6(10001)
    print(calc7())
