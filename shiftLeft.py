def shiftLeft(bitStr):
    bitStr = bitStr[1:] + bitStr[0]
    return bitStr


bitStr = input("Enter a string of bits:")

shiftLeftStr = shiftLeft(bitStr)
print("Shift left of", bitStr, "is:", shiftLeftStr)
