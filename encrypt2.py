def binaryStr(num):
    bitStr = "{0:b}".format(num)
    return bitStr


message = input("Enter a message:")
bitList = []
for b in message:
    bit = binaryStr(ord(b) + 1)
    bit = bit[1:] + bit[0]
    bitList.append(bit)
output = ""
for bit in bitList:
    output += bit + " "
print(output)
