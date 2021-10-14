s = "HelLo WorLd!!"

# Solution : {'o': 2, 'r': 1, 'h': 1, '!': 2, 'l': 3, 'e': 1, 'w': 1, 'd': 1}
res = {}
for c in s:
    if c != ' ':
        if c in res:
            res[c] += 1
        else:
            res[c] = 1
print(res)
