def codeStr(b=''):
    return chr(int(b, 2) - 1)


def shift(n=''):
    temp = list(n)
    new = (temp[-1:] + temp[0:-1])
    ret = ''

    for w in new:
        ret += w
    return ret


code = input("Enter the coded text:")
word = code.split()
decode = ''

for d in word:
    decode += codeStr(shift(d))
print(decode)
