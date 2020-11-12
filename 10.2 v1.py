""" Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out 
from the 'From ' line by finding the time and then splitting the string a second time using a colon. From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below. """

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

hours = dict()
lst = list()

for line in handle:
    # line = line.strip()                       # remove spaces at the beginning and at the end of the string
    if not line.startswith("From ") : continue
    hour = line.split()                         # split the string into a list hour, everything that start with "From "
    # print(hour)
    hr = hour[5].split(":")                     # split the string again into the list hr, but by the index 5
    # print(hr)
    hours[hr[0]] = hours.get(hr[0], 0) + 1      # do a histogram of hours, get the new value, and increase the counter
    # print(hours)

for v,k in hours.items():                       # k is hour, v is count
    lst.append((v, k))                          # append tuples to the list

lst.sort()                                      # sort the list by hour
for k,v in lst:                                 # for loop through list of tuples
    print(k, v)                                 # print counts sorted by hour
