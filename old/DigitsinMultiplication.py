import math

def f(A, B):
    digit_A = len(str(A))
    digit_B = len(str(B))

    return max(digit_A, digit_B)

n = int(input())

ans = 99999

for i in range(1, math.floor(math.sqrt(n)) + 1):
    if n % i != 0:
        continue
    A = i
    B = n // i
    ans = min(ans, f(A, B))

print(ans)
