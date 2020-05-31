n = int(input())
h = list(map(int, input().split()))

cost = [float('inf')] * n
cost[0] = 0
cost[1] = abs(h[1] - h[0])

for i in range(2, n):
    one_step = abs(h[i] - h[i - 1]) + cost[i - 1]
    two_step = abs(h[i] - h[i - 2]) + cost[i - 2]
    cost[i] = min(one_step, two_step)

print(cost[n - 1])