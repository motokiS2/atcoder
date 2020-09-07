import sys
import copy

sys.setrecursionlimit(10**7)

h, w, k = map(int, input().split())

c = [list(input()) for i in range(h)]

black = 0
for row in c:
    black += row.count("#")

# 消したい#の数
goal_b = k - black


