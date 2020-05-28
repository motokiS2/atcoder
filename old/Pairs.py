# n, k = map(int, input().split())
# a = list(map(int, input().split()))
# multi_list = []
# for i in range(len(a) - 1) :
#     for j in range(i + 1, len(a)) :
#         multi_list.append(a[i] * a[j])

# multi_list.sort()

# print(multi_list[k - 1])

n, k = map(int, input().split())
a = list(map(int, input().split()))

minus_nums = []
plus_nums = []
zeroes = []

for num in a :
    if num < 0 :
        minus_nums.append(num)
    elif num > 0 :
        plus_nums.append(num)
    elif num == 0 :
        zeroes.append(num)

minus_num = len(minus_nums)
plus_num = len(plus_nums)
zero_num = len(zeroes)

multi_minus_num = minus_num * plus_num
multi_plus_num = (minus_num * (minus_num - 1)) // 2 + (plus_num * (plus_num - 1)) // 2
zero_num = (minus_num + plus_num) * zero_num + (zero_num * (zero_num - 1)) // 2
;
ans = []

if k <= multi_minus_num :
    for minus in minus_nums :
        for plus in plus_nums :
            ans.append(plus * minus)
    ans.sort()
    print(ans[k - 1])
elif multi_minus_num < k <= multi_minus_num + zero_num :
    print(0)
elif multi_minus_num + zero_num < k :
    if minus_num != 1 :
        for i in range(minus_num - 1) :
            for j in range(i + 1, minus_num) :
                ans.append(minus_nums[i] * minus_nums[j])
    if plus_num != 1 :
        for i in range(plus_num - 1) :
            for j in range(i + 1, plus_num) :
                ans.append(plus_nums[i] * plus_nums[j])
    ans.sort()
    print(ans[k - (multi_minus_num + zero_num) - 1])