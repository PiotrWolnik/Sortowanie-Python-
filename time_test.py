#!/usr/bin/python
# -*- coding: utf-8 -*-

from sort import quicksort, bubblesort, check_list, random_list, list_n_
from timeit import timeit

t1_bubble: float = 0.0
t2_bubble: float = 0.0
t3_bubble: float = 0.0
t4_bubble: float = 0.0

t1_quick: float = 0.0
t2_quick: float = 0.0
t3_quick: float = 0.0
t4_quick: float = 0.0

for i in range(1000):
    t1_bubble += timeit(f"{bubblesort(check_list)}", number=1, globals=globals())
    t2_bubble += timeit(f"{bubblesort(list(reversed(check_list)))}", number=1, globals=globals())
    t3_bubble += timeit(str(bubblesort(random_list)), number=1, globals=globals())
    t4_bubble += timeit(f"{bubblesort(list_n_)}", number=1, globals=globals())

    t1_quick += timeit(f"{quicksort(check_list)}", number=1, globals=globals())
    t2_quick += timeit(f"{quicksort(list(reversed(check_list)))}", number=1, globals=globals())
    t3_quick += timeit(f"{quicksort(random_list)}", number=1, globals=globals())
    t4_quick += timeit(f"{quicksort(list_n_)}", number=1, globals=globals())

print(f"An average time for t1_bubble = {t1_bubble/1000}")
print(f"An average time for t2_bubble = {t2_bubble/1000}")
print(f"An average time for t3_bubble = {t3_bubble/1000}")
print(f"An average time for t4_bubble = {t4_bubble/1000}")

print(f"An average time for t1_quick = {t1_quick/1000}")
print(f"An average time for t2_quick = {t2_quick/1000}")
print(f"An average time for t3_quick = {t3_quick/1000}")
print(f"An average time for t4_quick = {t4_quick/1000}")

# Piotr Wolnik, 403077