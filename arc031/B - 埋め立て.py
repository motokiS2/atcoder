import sys
import copy

sys.setrecursionlimit(10**7)

a = [list(input()) for i in range(10)]


def dfs(x, y):
    if x < 0 or 10 <= x or y < 0 or 10 <= y:
        return
    if filled_a[x][y] == 'x':
        return

    filled_a[x][y] == 'x'

    dfs(x, y + 1)
    dfs(x, y - 1)
    dfs(x + 1, y)
    dfs(x - 1, y)

sx, sy = 0, 0
for i in range(10):
    for j in range(10):
        if a[i][j] == "o":
            sx, sy = i, j
            break
    else:
        continue
    break

for i in range(10):
    for j in range(10):
        filled_a = copy.deepcopy(a)

        filled_a[i][j] = "o"

        dfs(sx, sy)

        for k in range(10):
            if "o" in filled_a[k]:
                break
        else:
            print("YES")
            sys.exit()

print("NO")