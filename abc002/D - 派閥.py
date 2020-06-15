from itertools import *

n, m = map(int, input().split())
rel = [[0 for i in range(n)] for j in range(n)]
for _ in range(m):
    x, y = map(int, input().split())
    rel[x - 1][y - 1] = 1
    rel[y - 1][x - 1] = 1

ans = 1

for i in range(n, 1, -1):
    for comb in combinations(range(n), i):
        for c in combinations(comb, 2):
            if rel[c[0]][c[1]] == 0:
                break
        else:
            print(i)
            exit()

print(ans)