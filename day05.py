def bubble_sort(list):
    list_length = len(list) - 1
    for i in range(list_length):
        for j in range(len(list) - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
    return list

print(bubble_sort([8,-11,9,1]))