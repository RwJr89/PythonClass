def main():

    userList = [3, 1, 7, 1, 4, 10]
    print("List:", userList)
    print("Mode:", mode(userList))
    print("Median:", median(userList))
    print("Mean:", mean(userList))


def median(userList):
    if len(userList) == 0:
        return 0
    userList.sort()
    midIndex = int(len(userList) / 2)
    if len(userList) % 2 == 1:
        return userList[midIndex]
    else:
        return (userList[midIndex] + userList[midIndex - 1]) / 2


def mean(userList):
    if len(userList) == 0:
        return 0
    total = 0
    for number in userList:
        total += number
    return total / len(userList)


def mode(userList):
    if len(userList) == 0:
        return 0
    numberDictionary = {}
    for digit in userList:
        number = numberDictionary.get(digit, None)
        if number == None:
            numberDictionary[digit] = 1
        else:
            numberDictionary[digit] = number + 1
    maxValue = max(numberDictionary.values())
    modeList = []
    for key in numberDictionary:
        if numberDictionary[key] == maxValue:
            modeList.append(key)
    return modeList


main()
