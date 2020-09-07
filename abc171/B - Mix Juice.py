k, n = map(int, input().split())

p = list(map(int, input().split()))

p_sort = p.sort()

ans = sum(p[:n])

print(ans)