import math

a, b, h, m = map(int, input().split())

alpha = 1 / 6 * h * math.pi + 1 / 360 * m * math.pi
beta = m * math.pi / 30

x_a = a * math.sin(alpha)
y_a = a * math.cos(alpha)
x_b = b * math.sin(beta)
y_b = b * math.cos(beta)

ans = math.sqrt((x_a - x_b) ** 2 + (y_a - y_b) ** 2)

print(ans)