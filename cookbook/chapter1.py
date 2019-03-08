"""
    desc: cookbook notes
    link: https://python3-cookbook.readthedocs.io/zh_CN/latest/index.html
"""
import sys
import os
from collections import deque
import heapq


def avg(number):
    length = len(number)
    if length == 0:
        return 0
    else:
        return sum(number) / length


def drop_first_last(grades):
    first, *middle, last = grades
    return avg(middle)


def get_phone_numbers(info):
    name, email, *phone_numbers = info
    print('name=%s,email=%s,phone=%s' % (name, email, phone_numbers))


def do_foo(x, y):
    print('foo', x, y)


def do_bar(s):
    print('bar', s)


def tag_tuple():
    """
        desc: 带标签的元组序列分割
    """
    records = [
        ('foo', 1, 2),
        ('bar', 'hello'),
        ('foo', 3, 4),
    ]
    for tag, *args in records:
        if tag == 'foo':
            do_foo(*args)
        elif tag == 'bar':
            do_bar(*args)


def filter_mid_factor():
    # 过滤中间的元素
    line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
    print(line.split(':'))
    uname, *fileds, homedir, sh = line.split(':')
    print(uname, homedir, sh)


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)


def return_last_n_line():
    with open('chapter1_3.txt') as f:
        for line, prevlines in search(f, 'python', 5):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-' * 20)


def get_largest_smallest():
    """
    从列表里获得最大/小的N个数
    :return:
    """
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    print('largest:', heapq.nlargest(3, nums))
    print('smallest:', heapq.nsmallest(3, nums))


def complex_get_largest_smallest():
    """
    从复杂的数据结构中获得指定关键字最大/小的N个
    nlargest和nsmallest都可接受一个关键字参数，用于指定使用哪个值进行比较
    :return:
    """
    portfolio = [
        {'name': 'IBM', 'shares': 100, 'price': 91.1},
        {'name': 'AAPL', 'shares': 50, 'price': 543.22},
        {'name': 'FB', 'shares': 200, 'price': 21.09},
        {'name': 'HPQ', 'shares': 35, 'price': 31.75},
        {'name': 'YHOO', 'shares': 45, 'price': 16.35},
        {'name': 'ACME', 'shares': 75, 'price': 115.65}
    ]
    cheap = heapq.nsmallest(3, portfolio, key=lambda x: x['price'])
    expensive = heapq.nlargest(3, portfolio, key=lambda x: x['price'])
    print(cheap)
    print(expensive)

def heap_pop():
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(heapq.heappop(nums))
    print(heapq.heappop(nums))
    print(heapq.heappop(nums))
    print(nums)

def sort_cut():
    """
    查找最大的N个数或者最小的N个数，若集合大小与N的大小接近，先排序再切片会更快点
    若不接近，直接用nlargest和nsmallest会更方便
    :return:
    """
    items = [1,2,3,4,5,6,7,8,9]
    N = 8
    print(sorted(items)[-N:])

if __name__ == '__main__':
    sort_cut()
    pass
