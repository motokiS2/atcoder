import math

x = int(input())

money = 100
year = 0

while True:
    money = math.floor(money * 1.01)
    year += 1
    if money >= x:
        break

print(year)