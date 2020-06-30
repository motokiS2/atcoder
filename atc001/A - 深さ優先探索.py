import sys

sys.setrecursionlimit(10**7)

h, w = map(int, input().split())
c = [list(input()) for _ in range(h)]


def dfs(x, y):
    if x < 0 or w <= x or y < 0 or h <= y:
        return
    elif c[y][x] == "#":
        return
    elif c[y][x] == "g":
        print("Yes")
        sys.exit()

    c[y][x] = "#"

    dfs(x, y+1)
    dfs(x, y-1)
    dfs(x+1, y)
    dfs(x-1, y)


sx, sy = 0, 0

for i in range(h):
    for j in range(w):
        if c[i][j] == "s":
            sx, sy = j, i
            break

dfs(sx, sy)
print("No")

