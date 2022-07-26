
# You may only use the following functions to construct your code:
#
# python builtin sum()
# python builtin max()
# python builtin min()
# python Math function Math.sqrt()
# python normal operators on floats (*, /, +, -, etc)

import math
from typing import List



def zcount(list: List[float]) -> float:
    """
    Count of numbers in list
    :param list:
    :return:
    """
    return(len(list))


def zmean(list: List[float]) -> float:
    """
    mean = sum(data0) / count(data0)
    :param list:
    :return:
    """
    return sum(list) / zcount(list)


def zmode(list: List[float]) -> float:
    """
    the mode is the most common value in list
    :param list:
    :return:
    """
    return max(set(list), key=list.count)


def zmedian(list: List[float]) -> float:
    """
    The median is the middle value
    :param list:
    :return:
    """
    sorted_number = sorted(list)
    list_len = len(list)
    index = (list_len - 1) // 2
    if list_len % 2 == 0:
        return sorted_number[index]
    else:
        return(sorted_number[index] + sorted_number[index +1])/2


