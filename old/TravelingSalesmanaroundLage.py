k, n = map(int, input().split())
a = list(map(int, input().split()))

a.append(a[0] + k)

max_distance = a[1] - a[0]
for i in range(n):
    if a[i + 1] - a[i] > max_distance:
        max_distance = a[i + 1] - a[i]

print(k - max_distance)