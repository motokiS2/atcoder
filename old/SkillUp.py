n, m, x = map(int, input().split())
c_a = []

for i in range(n):
    c_a.append(list(map(int, input().split())))

new_c_a = sorted(c_a)


test = [0] * m

for i in range(n):
    for j in range(m):
        test[j] += new_c_a[i][j + 1]

for num in test:
    if num < x:
        print(-1)
        exit()

