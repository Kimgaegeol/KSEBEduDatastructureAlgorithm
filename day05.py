import time
import random

def time_decorator(func):
    def wrapper(*arg):
        s = time.time()
        r = func(*arg)
        e = time.time()
        print(f'실행시간 : {e-s}초')
        return r
    return wrapper

@time_decorator
def my_bubble_sort(list):
    list_length = len(list) - 1
    for i in range(list_length):
        for j in range(i+1,len(list)):
            if list[i] > list[j]:
                list[i], list[j] = list[j], list[i]
    return list

@time_decorator
def bubble_sort(l):
    for i in range(len(l) - 1):
        for j in range(len(l) - 1 - i):
            if l[j] > l[j+1]:
                l[j], l[j + 1] = l[j+1], l[j]
            #print(j, end=' ')
    return l

@time_decorator
def bubble_sort_tuning(l):
    for i in range(len(l) - 1):
        no_swap = True
        for j in range(len(l) - 1 - i):
            if l[j] > l[j+1]:
                l[j], l[j + 1] = l[j+1], l[j]
                no_swap = False
        if no_swap:
            return l
    return l

@time_decorator
def insert_sort(l):
    for i in range(1, len(l)):
        value = l[i]
        while i > 0 and l[i-1] > value:
            l[i] = l[i-1]
            i = i-1
        l[i] = value
    return l

lists1 = [random.randint(1,10000) for _ in range(10000)]
lists2 = lists1.copy()
lists3 = lists1.copy()
lists4 = lists1.copy()

print(bubble_sort(lists1))
print(bubble_sort_tuning(lists2))
print(my_bubble_sort(lists3))
print(insert_sort(lists4))
