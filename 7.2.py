""" Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form: X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. 
Do not use the sum() function or a variable named sum in your solution. """

# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname, "r")

count = 0
total = 0.0 # because is a float
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    f = line.find(":")                                          # return the index of ":", # print(f) to show the index
    total = total + float(line[f+2:])                           # slicing the number, convert to a float and sum
    count = count + 1                                           # count every line and sum
print("Average spam confidence:", total / count)


# Inicial code
# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname, "r")

count = 0
total = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count = count + 1                                           # count every line
    f = line.find(":")                                          # return the index of ":", # print(f) to show the index
    num = line[f+2:]
    f = (float(num, 4))                                         # convert the string to a number with 4 decimals
    total = total + f                                           # do a sum of f
    average = total / count                                     # average of sum of total of lines with number of lines
print("Average spam confidence:", average)
