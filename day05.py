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

def quick_sort(l):
    n = len(l)
    if n<=1: return l
    pivot = l[n//2]
    left, mid, right = list(), list(), list()

    for i in l:
        if i < pivot:
            left.append(i)
        elif i > pivot:
            right.append(i)
        else:
            mid.append(i)

    return quick_sort(left)+mid+quick_sort(right)

if __name__ == '__main__':
    lists1 = [random.randint(1,100000) for _ in range(100000)]
    lists2 = lists1.copy()
    lists3 = lists1.copy()
    lists4 = lists1.copy()
    lists5 = lists1.copy()

    # print(bubble_sort(lists1))
    # print(bubble_sort_tuning(lists2))
    # print(my_bubble_sort(lists3))
    # print(insert_sort(lists4))

    s = time.time()
    print(quick_sort(lists5))
    e = time.time()
    print(f'실행시간 : {e - s}초')