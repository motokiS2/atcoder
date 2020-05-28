n = int(input())
words = {}
# 各文字列の登場回数を辞書に格納
for i in range(n) :
    new_word = input()
    if new_word in words.keys() :
        words[new_word] += 1
    else :
        words[new_word] = 1

# max_val = max(words.values())
# keys_of_max_val = [key for key in words if words[key] == max_val]

# keys_of_max_val.sort()


# for word in keys_of_max_val :
    # print(word)

mx_freq = max(words.values())
mx_words = [k for k, v in words.items() if words[k] == mx_freq]
# ↓はWAになるなぜ
# mx_words = [k for k, v in words.items() if v == mx_freq]

mx_words.sort()

for mx_word in mx_words :
    print(mx_word)