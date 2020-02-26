def shiftRight(bitStr):
    bitStr = bitStr[len(bitStr) - 1] + bitStr[0:len(bitStr) - 1]
    return bitStr


bitStr = input("Enter a string of bits:")
shiftRightStr = shiftRight(bitStr)
print("Shift right of", bitStr, "is:", shiftRightStr)
