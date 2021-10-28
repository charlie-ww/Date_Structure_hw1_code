# code from https://www.geeksforgeeks.org/hoares-vs-lomuto-partition-scheme-quicksort/


def partition(arr, low, high):
    pivot = arr[low]
    i = low - 1
    j = high + 1

    while (True):

		# Find leftmost element greater than
		# or equal to pivot
        i += 1
        while (arr[i] < pivot):
            i += 1

		# Find rightmost element smaller than
		# or equal to pivot
        j -= 1
        while (arr[j] > pivot):
            j -= 1

        # If two pointers met.
        if (i >= j):
            return j

        arr[i], arr[j] = arr[j], arr[i]


''' The main function that implements QuickSort
arr --> Array to be sorted,
low --> Starting index,
high --> Ending index '''


def quickSort(arr, low, high):
	''' pi is partitioning index, arr[p] is now
	at right place '''
	if (low < high):

		pi = partition(arr, low, high)

		# Separately sort elements before
		# partition and after partition
		quickSort(arr, low, pi)
		quickSort(arr, pi + 1, high)


from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws['A1'] = '時間'

import numpy as np
import time



for a in range(10, 26):
    n = 2 ** a
    ws.append(["2的", a])
    for k in range(10):

        random_list = np.random.randint(0, 1001, size=n)
        # print("Given array is")
        # for x in range(n):
        #     print("%d" % random_list[x]),
        start = time.time()
        quickSort(random_list, 0, n-1)
        end = time.time()
        # print("\n\nSorted array is")
        # for i in range(n):
        #     print("%d" % random_list[i]),
        print("use ", end-start, "time")

        ws.append([end-start])
wb.save("hoare.xlsx")