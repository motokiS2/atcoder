S = input()

N = len(S)

S_2 = S[:(N-1)//2]
S_3 = S[(N+3)//2 - 1:N]

if S == S[::-1] and S_2 == S_2[::-1] and S_3 == S_3[::-1]:
    print('Yes')
else:
    print('No')