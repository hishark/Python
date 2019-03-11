"""
    desc: cookbook notes
    link: https://python3-cookbook.readthedocs.io/zh_CN/latest/index.html
"""
import sys
import os
import json
from collections import deque
import heapq
from collections import defaultdict
from collections import OrderedDict


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
    items = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    N = 8
    print(sorted(items)[-N:])


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        """
        队列包含了一个 (-priority, index, item) 的元组。
        优先级为负数的目的是使得元素按照优先级从高到低排序。
        这个跟普通的按优先级从低到高排序的堆排序恰巧相反。

        index 变量的作用是保证同等优先级元素的正确排序。
        通过保存一个不断增加的 index 下标变量，可以确保元素按照它们插入的顺序排序。
        而且， index 变量也在相同优先级元素比较的时候起到重要作用。
        """
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Item:
    def __init__(self, name):
        self.name = name

    # https://blog.csdn.net/luckytanggu/article/details/53649156
    # __repr__的用处
    def __repr__(self):
        return 'Item(%s)' % self.name


def show_priority_queue():
    q = PriorityQueue()
    q.push(Item('cool'), 3)
    q.push(Item('hishark'), 5)
    q.push(Item('777'), 4)
    q.push(Item('guy'), 2)
    q.push(Item('๑乛◡乛๑'), 1)
    i = 0
    while i < 5:
        print(q.pop())
        i += 1


def multidict():
    """
    一个键对应多个值的字典
    :return:
    """
    #
    d = defaultdict(list)
    d['a'].append(1)
    d['a'].append(2)
    d['a'].append(3)
    print(d)

    d = defaultdict(set)
    d['a'].add(1)
    d['a'].add(1)
    d['a'].add(2)
    print(d)

    d = defaultdict(list)
    pairs = [('a', 'Ah...'), ('a', 'movie!!!'), ('a', 'yeah!!!')]
    for key, value in pairs:
        d[key].append(value)
    print(d)


def control_dict_order():
    """
    控制字典中元素的顺序
    使用ordereddict类，在迭代操作时它会保持元素被插入时的顺序

    当你想要构建一个将来需要序列化或编码成其他格式的映射的时候，
    OrderedDict 是非常有用的。
    比如，你想精确控制以 JSON 编码后字段的顺序，
    你可以先使用 OrderedDict 来构建这样的数据
    :return:
    """
    d = OrderedDict()
    d['hello'] = 1
    d['what'] = 2
    d['hungry'] = 3
    d['too'] = 4
    for key in d:
        print(key, d[key])
    print(json.dumps(d))


def dict_operation():
    """
    字典的运算
    :return:
    """
    prices = {
        'ACME': 45.23,
        'AAPL': 612.78,
        'IBM': 205.55,
        'HPQ': 37.20,
        'FB': 10.75
    }
    print(prices)
    # zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。
    # zip 方法在 Python 2 和 Python 3 中的不同：在 Python 3.x 中为了减少内存，zip() 返回的是一个对象。如需展示列表，需手动 list() 转换。
    print(list(zip(prices.values(), prices.keys())))
    prices_and_names = zip(prices.values(), prices.keys())
    # zip创建的是一个只能访问一次的迭代器，若继续输出max会报错
    print('min=', min(prices_and_names))
    # print('max=',max(prices_and_names))

    prices_sorted = sorted(zip(prices.values(), prices.keys()))
    # sorted之后输出两次没得错
    print('sorted:', prices_sorted)
    print('sorted:', prices_sorted)


def dict_same_point():
    """
    查找两字典的相同点
    :return:
    """
    a = {
        'x': 1,
        'y': 2,
        'z': 3
    }
    b = {
        'w': 10,
        'x': 11,
        'y': 2
    }
    print('same keys:', a.keys() & b.keys())
    # 如果你想对集合的键执行一些普通的集合操作，可以直接使用键视图对象而不用先将它们转换成一个set
    print('a - diff keys:', a.keys() - b.keys())
    print('same values:', a.items() & b.items())
    # 下面这行values&values会报错--[TypeError: unsupported operand type(s) for &: 'dict_values' and 'dict_values']
    # 无法使用.values()找共同值噢
    # print('same values:', a.values() & b.values())
    c = {key: a[key] for key in a.keys() - {'z', 'w'}}
    print(c)


def dedupe(items):
    """
    删除序列相同元素 - 值为hashable类型的序列
    :param items:
    :return:
    """
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)
            print('seen=', seen)


def dedupe_example():
    """
    删除序列的相同元素 example
    :return:
    """
    a = [1, 5, 2, 1, 9, 1, 5, 10]
    for x in dedupe(a):
        print(x)
    # print(list(dedupe(a)))


if __name__ == '__main__':
    dedupe_example()
    pass
