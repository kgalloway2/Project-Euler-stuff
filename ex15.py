# this imports the argv module to allow us to input variables before running the program
from sys import argv

# this defines the variables script and filename as the inputs given when starting the program
script, filename = argv

# this defines txt as the function which opens filename
txt = open(filename)

# this just prints a sting with a formatted variable
print "Here's your file %r:" % filename
# this prints the function txt (which is open filename) as read only and then closes the file after printing
print txt.read()
txt.close()

#this is a string and defines file_again as the input
print "Type the filename again:"
file_again = raw_input("> ")

# this defines txt_again as a function kinda like before
txt_again = open(file_again)


# this prints the function txt_again like line 13 and then closes the file after printing
print txt_again.read()
txt_again.close()