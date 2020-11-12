""" Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' 
lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address
to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop 
to find the most prolific committer. """

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt" # Para colocar que el valor predeterminado es "mbox-short.txt" y presionar enter
handle = open(name, 'r')

sender = dict()
for line in handle:
    line = line.rstrip()                              # also line.strip() to remove blank spaces 
    if not line.startswith("From ") : continue        # if the line does not start with "From " then continue
    email = line.split()
    sender[email[1]] = sender.get(email[1],0) + 1     # do a histogram of words email, get the new value and increase the counter

# print(sender)
lgest = None
lgest_sender = None

for key in sender:                                    # for loop to the largest sender
    if lgest is None:
        lgest = sender[key]

    if lgest < sender[key]:
            lgest = sender[key]
            lgest_sender = key

print(lgest_sender, lgest)
