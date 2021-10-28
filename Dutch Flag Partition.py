# code from https://www.techiedelight.com/quicksort-using-dutch-national-flag-algorithm/
def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp


# Partition routine using the Dutch national flag algorithm
def partition(A, start, end):
    mid = start
    pivot = A[end]

    while mid <= end:

        if A[mid] < pivot:
            swap(A, start, mid)
            start += 1
            mid += 1

        elif A[mid] > pivot:
            swap(A, mid, end)
            end -= 1

        else:
            mid += 1

    # `A[start … mid-1]` contains all occurrences of a pivot
    return start - 1, mid


# 3–way Quicksort routine
def quicksort(A, start, end):
    # base condition for 0 or 1 elements
    if start >= end:
        return

    # handle 2 elements separately as the Dutch national flag
    # algorithm will work for 3 or more elements
    if start - end == 1:
        if A[start] < A[end]:
            swap(A, start, end)
        return

    # rearrange elements across pivot using the Dutch
    # national flag problem algorithm
    x, y = partition(A, start, end)

    # recur on sublist containing elements that are less than the pivot
    quicksort(A, start, x)

    # recur on sublist containing elements that are more than the pivot
    quicksort(A, y, end)
from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws['A1'] = '時間'

import numpy as np
import time


# arr = [12, 11, 13, 5, 6, 7]
# n = len(random_list)
# 26
for a in range(10, 26):
    n = 2 ** a
    ws.append(["2的", a])
    for k in range(10):

        random_list = np.random.randint(0, 1001, size=n)
        # print("Given array is")
        # for x in range(n):
        #     print("%d" % random_list[x]),
        start = time.time()
        quicksort(random_list, 0, n - 1)
        end = time.time()
        # print("\n\nSorted array is")
        # for i in range(n):
        #     print("%d" % random_list[i]),
        print("use ", end-start, "time")

        ws.append([end-start])
wb.save("dutch.xlsx")