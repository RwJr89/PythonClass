# Write a script named copyFile.py.
# This script should prompt the user
# for the names of two text files.
# The contents of the first file
# should be input and written to the second file.

# An example of the program input is shown below:
# Enter the input file name: copyFrom.txt
# Enter the output file name: copyTo.txt


inFileName = input("Enter the input file name:")
outFileName = input("Enter the output file name:")
inputFile = open('copyFrom.txt', 'r')
outputFile = open('copyTo.txt', "w")
line = ""
for line in inputFile:
    outputFile.write(line)
inputFile.close()
outputFile.close()
