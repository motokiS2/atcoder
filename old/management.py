n = int(input())
a = list(map(int, input().split()))

number_subordinate = [0] * n

for i in a:
    number_subordinate[i - 1] += 1


for number in number_subordinate:
    print(number)