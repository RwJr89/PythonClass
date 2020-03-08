# Rep to Decimal


def repToDecimal(str, base):
    result = 0

    dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
            '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    for r in str:
        n = dict[r]
        result = base * result + n
    return result


print(repToDecimal('10', 10))
print(repToDecimal('10', 8))
print(repToDecimal('10', 2))
print(repToDecimal('10', 16))


# Decimal to Rep

def decimalToRep(num, base):
    result = ""
    while (num > 0):
        rem = num % base
        if rem in range(10):
            result += str(rem)
        else:
            result += chr(65 + (rem % 10))
        num = num // base
    result = result[::-1]
    if (result == ""):
        return '0'
    return result


def main():
    """Tests the function."""
    print(decimalToRep(10, 10))
    print(decimalToRep(10, 8))
    print(decimalToRep(10, 2))
    print(decimalToRep(10, 16))
