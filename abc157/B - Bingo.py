import numpy as np

A = np.zeros((3, 3))
for i in range(3):
    A[i] = list(map(int, input().split()))

hit = np.zeros((3, 3))

N = int(input())
b = np.zeros((N, 1))

for i in range(N):
    b[i] = int(input())

for i in range(3):
    for j in range(3):
        if A[i][j] in b:
            hit[i][j] += 1

hit_T = hit.T

if hit[0][0] + hit[1][1] + hit[2][2] == 3 or \
    hit[0][2] + hit[1][1] + hit[2][0] == 3:
    print('Yes')
    exit()

for i in range(3):
    if sum(hit[i]) == 3:
        print('Yes')
        exit()
    if sum(hit_T[i]) == 3:
        print('Yes')
        exit()

print('No')