n, k = map(int, input().split())  # "7 3"

l = [i + 1 for i in range(n)]
head = -1
count = 0
result = []
while True:
    if len(result) == n:
        break
    head = (head + 1) % n
    if l[head] is None:
        pass
    else:
        count = count + 1
        if count == k:
            result.append(l[head])
            l[head] = None
            count = 0

print("<"+", ".join(map(str, result))+">")  # <3, 6, 2, 7, 5, 1, 4>
