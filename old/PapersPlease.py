n = int(input())
a = list(map(int, input().split()))
# even_list = []
# for num in a:
#     if num % 2 == 0 :
#         even_list.append(num)

# deny = 0
# for even in even_list :
#     if even % 3 != 0 and even % 5 != 0 :
#         deny = 1
#         break

# if deny == 0 :
#     print('APPROVED')
# else :
#     print('DENIED')

for num in a :
    if num % 2 == 1 :
        continue
    if num % 3 != 0 and num % 5 != 0 :
        print('DENIED')
        break
else :
    print('APPROVED')