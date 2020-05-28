N = int(input())
S = input()

R = S.count('R')
G = S.count('G')
B = S.count('B')

ans = R * G * B

for i in range(N):
    for j in range(i + 1, N):
        if S[i] != S[j]:
            k = 2 * j - i
            if k >= N:
                break
            if S[i] != S[j] and S[i] != S[k] and S[j] != S[k]:
                ans -= 1

print(ans)