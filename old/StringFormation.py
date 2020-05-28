from collections import deque

S = input()
Q = int(input())

# T = ""
# for i in range(Q) :
#     Query = list(input().split())
#     if Query[0] == "1" :
#         S, T = T, S
#     elif Query[0] == "2" :
#         if Query[1] == "1" :
#             T = T + Query[2]
#         elif Query[1] == "2" :
#             S = S + Query[2]

# T = T[::-1]
# T = T + S
# print(T)

d = deque(S)

rev = False
for i in range(Q) :
    Query = list(input().split())
    if Query[0] == "1" :
        rev = not rev
    else :
        Query[1] = int(Query[1])
        if rev :
            Query[1] = 3 - Query[1]
        if Query[1] == 1 :
            d.appendleft(Query[2])
        else :
            d.append(Query[2])

if rev :
    d.reverse()
ans = ""
for s in d :
    ans += s
print(ans)