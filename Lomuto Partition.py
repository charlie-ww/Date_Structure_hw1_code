# code from https://gist.github.com/betandr/e402f08bdf426ab4d6774418da63689f
import sys
sys.setrecursionlimit(3000)
def _partition(array, lo, hi):
    pivot = array[hi]

    i = lo - 1
    for j in range(lo, hi):
        if array[j] < pivot:
            i += 1
            temp = array[i]
            array[i] = array[j]
            array[j] = temp
    temp = array[i + 1]
    array[i + 1] = array[hi]
    array[hi] = temp
    return i + 1

def _quicksort(array, lo, hi):
    if lo < hi:
        p = _partition(array, lo, hi)
        _quicksort(array, lo, p - 1)
        _quicksort(array, p + 1, hi)
    return array

def quicksort(array):
    return _quicksort(array, 0, len(array) - 1)

from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws['A1'] = '時間'

import numpy as np
import time


# arr = [12, 11, 13, 5, 6, 7]
# n = len(random_list)
for a in range(10, 23):
    n = 2 ** a
    ws.append(["2的", a])
    for k in range(10):

        random_list = np.random.randint(0, 1001, size=n)
        print("Given array is")
        for x in range(n):
            print("%d" % random_list[x]),
        start = time.time()
        quicksort(random_list)
        end = time.time()
        print("\n\nSorted array is")
        for i in range(n):
            print("%d" % random_list[i]),
        print("use ", end-start, "time")

        ws.append([end-start])
wb.save("lomuto.xlsx")
# This code is contributed by Mohit Kumra