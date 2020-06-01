import collections

def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

n = int(input())

ans = 0

c = collections.Counter(prime_factorize(n))

for key in c.keys():
    for i in range(1, c[key] + 1):
        if n % (key ** i) == 0:
            n //= (key ** i)
            ans += 1


print(ans)