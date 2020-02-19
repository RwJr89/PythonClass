coded = input("Enter the coded text: ")
distance = int(input("Enter the distance: "))
text = ""

for ch in coded:
    ordval = ord(ch)
    cipval = ordval - distance
    text += chr(cipval)
print(text)
