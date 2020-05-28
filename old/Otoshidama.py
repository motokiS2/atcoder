n, y = map(int, input().split())


for i in range(n + 1):
    for j in range(n - i + 1):
        k = n - (i + j)
        money = 10000 * i + 5000 * j + 1000 * k
        if money == y:
            print(i, j, k)
            break
    else:
        continue
    break
else:
    print(-1, -1, -1)