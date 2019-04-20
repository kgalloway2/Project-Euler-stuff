# this defines the variable x as a string with an integer input for its formatted variable
x = "There are %d types of people." % 10
# this defines binary 
binary = "binary"
# tis defines do_not as don't
do_not = "don't"
# this defines the variable y as a sting with two formatted variables which are also strings
y = "Those who know %s and those who %s." % (binary, do_not)

# this prints the variable x and inputs the formatted variable
print x
# this prints the variable y and inputs the formatted variabes
print y

# this prints a string with a formatted variable of x. the formatted variable then contains another formatted variable
print "I said: %r." % x
# this prints a string with y as a formatted variable. y also has formatted variables in it
print "I also said: '%s'." % y

# this defines hilarious as the value of False
hilarious = False
# this defines joke_evaluation as a string with a formatted variable, but does not yet define the input for the formatted variable
joke_evaluation = "Isn't that joke so funny?! %r"

# this prints the previous two variables, using hilarious as the input for the formatted variable of joke_evaluation
print joke_evaluation % hilarious

# this defines w as a string
w = "This is the left side of... "
# this defines e as a string
e = "a string with a right side. "

# this prints the string w combined with the string e, connecting them from the end of one to the beginning of the next.
print w + e

t = "It works!"

# let's try combining more than two strings
print w + e + t 