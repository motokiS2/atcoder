n = int(input())

ans = (10 ** (n - 1) - 9 ** (n - 1)) * n % (10 ** 9 + 7)

print(ans)