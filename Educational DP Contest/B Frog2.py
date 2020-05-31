import numpy as np

n, k = map(int, input().split())
h = list(map(int, input().split()))
h = np.array(h)

cost = np.array([10 ** 9] * n)

cost[0] = 0


for i in range(1, n):
    jump_cost = np.abs(h[max(i-k, 0):i] - h[i]) + cost[max(i-k, 0):i]
    cost[i] = min(jump_cost)

print(cost[n - 1])
