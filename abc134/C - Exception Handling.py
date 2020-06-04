n = int(input())

a = []

for _ in range(n):
    a.append(int(input()))

a_max = max(a)
a_max_index = a.index(a_max)

a.sort(reverse=True)
a_second_max = a[1]

for i in range(n):
    if i == a_max_index:
        print(a_second_max)
    else:
        print(a_max)