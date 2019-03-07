"""
    desc: cookbook notes
    link: https://python3-cookbook.readthedocs.io/zh_CN/latest/index.html
"""
import sys
import os


def avg(number):
    length = len(number)
    if length == 0:
        return 0
    else:
        return sum(number) / length


def drop_first_last(grades):
    first, *middle, last = grades
    return avg(middle)


if __name__ == '__main__':
    grades = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(drop_first_last(grades))
    print(">")