import math

def calc_distance(x_1, y_1, x_2, y_2):
    return math.sqrt((x_1 - x_2)**2 + (y_1 - y_2)**2)

n = int(input())
ans = 0

x = []
y = []

for _ in range(n):
    x_temp, y_temp = map(int, input().split())
    x.append(x_temp)
    y.append(y_temp)

for i in range(n - 1):
    for j in range(i + 1, n):
        ans = max(ans, calc_distance(x[i], y[i], x[j], y[j]))


print(ans)