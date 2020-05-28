import math


K = int(input())

sum = 0

for i in range(1, K + 1):
    for j in range(1, K + 1):
        sum += math.gcd(i, j)
        if j == K:
            break
        else:
            for k in range(j + 1, K + 1):
                sum += math.gcd(i, math.gcd(j, k)) * 2

print(sum)

