# this loads the argv modules from sys
from sys import argv

# this defines our argv inputs
script, input_file = argv

# this defines the print_all function to just print the entire file
def print_all(f):
    print f.read()

# this defines the rewind function which takes the text file back to the beginning
def rewind(f):
    f.seek(0)

# this defines the print_A_line function which takes the input of
# a line number and the file to be viewed
def print_a_line(line_count, f):
    print line_count, f.readline()

# this defines current_file as the function that opens the input file
current_file = open(input_file)

# the rest of this does all the printing stuff
print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1 
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)