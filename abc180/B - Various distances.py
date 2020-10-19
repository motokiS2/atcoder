import math

n = int(input())
x = list(map(int, input().split()))
x = list(map(abs, x))

manhattan = sum(x)

x_power = [xi**2 for xi in x]
euclidean = math.sqrt(sum(x_power))

chebyshev = max(x)

print(manhattan)
print(euclidean)
print(chebyshev)