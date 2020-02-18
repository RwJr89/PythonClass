text = input("Enter a message:")
distance = int(input("Enter the distance value:"))
code = ''

for ch in text:
    code += chr(ord(ch) + distance)
print("\n" + code)
