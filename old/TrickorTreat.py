n, k = map(int, input().split())

d = []
a = []

for i in range(k):
    d.append(int(input()))
    a.append(list(map(int,input().split())))


okashi = [0] * n


for i in a:
    for j in i:
        okashi[j-1] = 1

ans = n - sum(okashi)

print(ans)