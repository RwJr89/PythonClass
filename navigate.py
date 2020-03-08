fileName = input("Enter the input file name:")
lines = []
with open(fileName, "r") as f:
    for line in f:
        lines.append(line.strip())

while True:
    print("The file has", len(lines), "lines.")
    if len(lines) == 0:
        break
    lineNum = int(input("Enter a line number [0 to quit]:"))
    if lineNum == 0:
        break
    else:
        print(lineNum, ":", lines[lineNum - 1])
