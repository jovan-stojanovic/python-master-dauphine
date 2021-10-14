code = {'e':'a', 'l':'m', 'o':'e', 'a': 'e'}
s = 'Hello world!'
# s_code = 'Hamme wermd!'

s_code = []
for c in s:
    if c in code:
        s_code.append(code[c])
    else:
        s_code.append(c)
s_code = ''.join(s_code)
print(s_code)


### solution with str
s.translate(str.maketrans(code))
