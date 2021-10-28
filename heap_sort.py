# code from https://www.geeksforgeeks.org/python-program-for-heap-sort/
def heapify(arr, n, i):
    largest = i # Initialize largest as root
    l = 2 * i + 1	 # left = 2*i + 1
    r = 2 * i + 2	 # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root
    if l < n and arr[i] < arr[l]:
        largest = l

    # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r

    # Change root, if needed
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i] # swap

        # Heapify the root.
        heapify(arr, n, largest)

# The main function to sort an array of given size
def heapsort(arr):
    n = len(arr)

    # Build a maxheap.
    # Since last parent will be at ((n//2)-1) we can start at that location.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] # swap
        heapify(arr, i, 0)

from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws['A1'] = '時間'

import numpy as np
import time


# arr = [12, 11, 13, 5, 6, 7]
# n = len(random_list)
for a in range(10, 25):
    n = 2 ** a
    ws.append(["2的", a])
    for k in range(10):

        random_list = np.random.randint(0, 1001, size=n)
        # print("Given array is")
        # for x in range(n):
        #     print("%d" % random_list[x]),
        start = time.time()
        heapsort(random_list)
        end = time.time()
        # print("\n\nSorted array is")
        # for i in range(n):
        #     print("%d" % random_list[i]),
        print("use ", end-start, "time")

        ws.append([end-start])
wb.save("heap.xlsx")