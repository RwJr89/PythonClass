inputFileName = input("Enter input file name:")
outFileName = input("Enter output file name:")

with open(inputFileName, 'r')as x, open(outFileName, 'w')as y:
    num = 0
    for n in x:
        num += 1
        y.write('{:>4}> {}'.format(num, n))
