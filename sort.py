# Piotr Wolnik, 403077

import random
from typing import List, Tuple


def quicksort(I: List) -> List:
    '''This function is sorting a list via using pivot'''
    list_to_sort = I[:]

    def quicksort_inplace(I: List, start: int, stop: int):
        i = start
        j = stop
        pivot = I[(start+stop)//2]
        while i < j:
            while I[i] < pivot:
                i += 1
            while I[j] > pivot:
                j -= 1
            if i <= j:
                I[i], I[j] = I[j], I[i]
                i += 1; j -= 1
        if start < j:
            quicksort_inplace(I, start, j)
        if i < stop:
            quicksort_inplace(I, i, stop)
    quicksort_inplace(list_to_sort, 0, len(list_to_sort) - 1)

    return list_to_sort


def bubblesort(unsorted_list: List) -> Tuple[List, int]:
    how_many_operations: int = 0
    n = len(unsorted_list)
    flague = True
    if unsorted_list == sorted(unsorted_list):
        return unsorted_list, 0
    while n > 1 and flague:
        flague = False
        for i in range(1, n):
            how_many_operations += 1
            if unsorted_list[i - 1] > unsorted_list[i]:
                unsorted_list[i - 1], unsorted_list[i] = unsorted_list[i], unsorted_list[i - 1]
                flague = True
        n -= 1
    return unsorted_list, how_many_operations


check_list = [i for i in range(1000)]
random_list = random.sample(range(1, 1001), 1000)
list_n_ = [random.random()]*1000
