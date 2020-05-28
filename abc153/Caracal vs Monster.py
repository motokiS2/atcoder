h = int(input())

def dist(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    ret = 2 * dist(n // 2) + 1

    return ret

print(dist(h))