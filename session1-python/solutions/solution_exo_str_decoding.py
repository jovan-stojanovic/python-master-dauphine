s_code = 'Hamme wermd!'

revert_code = {}
for k, v in code.items():
    revert_code[v] = k

s_decode = []
for c in s_code:
    s_decode.append(revert_code.get(c, c))
s_decode = ''.join(s_decode)
print(s_decode)
