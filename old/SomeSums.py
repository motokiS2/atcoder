n = int(input())
a = list(map(int, input().split()))

alice = []
bob = []

a.sort(reverse=True)

for i in range(n):
    if i % 2 == 0:
        alice.append(a[i])
    else:
        bob.append(a[i])

ans = sum(alice) - sum(bob)

print(ans)