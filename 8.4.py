""" Open the file romeo.txt and read it line by line. For each line, split the line into a list
of words using the split() method. The program should build a list of words. For each word on each
line check to see if the word is already in the list and if not append it to the list.
When the program completes, sort and print the resulting words in alphabetical order.
You can download the sample data at http://www.py4e.com/code3/romeo.txt """

fname = input("Enter file name: ")
fh = open(fname)

lst = list()
for line in fh:
    line = line.split()
    for l in line:
        if l not in lst:
            lst.append(l)

print(sorted(lst))

# append text file into a list
fname = input("Enter file name: ")
fh = open(fname, "r")

lst = list()
for line in fh:
	lst.append(line)

print(lst)

# Append text file into a list and split
fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line = line.split()
    for l in line:
        lst.append(l)

print(lst)
