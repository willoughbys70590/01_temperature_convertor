# source: https://ww.guru99.com/reading-and-writing-files-in-python.html
import re

# Data to be out putted
data = ['I', 'Love', 'Computers']

# Get filenmae, cant be blank / invalid
# assume valid data for now

has_errors = "yes"
while has_errors == "yes":
    has_errors = "no"
    filename = input("Entre a filename (leave off the extension): ")

    valid_char = "[A-Za-a0-9-]"
    for letter in filename:
        if re.match(valid_char, letter):
            continue

        elif letter == " ":
            problem = "(no spaces allowed)"
        else:
            problem = ("(no {}'s allowed".format(letter))
            has_errors = "yes"

    if filename == "":
        problem = "Cant be blank"
        has_errors = "yes"

    if has_errors == "yes":
        print("invalid filename - {}".format(problem))
        print()
    else:
        print("You entred a valid filename")


# add .txt stuffix!
filename = filename + ".txt"

# create file to hold data
f = open(filename, "w+")

# add new line at the end of each item
for item in data:
    f.write(item +"\n")

# close file
f.close()
