print "Which file do you want to open?"
filename = open(raw_input("> "), "w")
#print "Which line of this file do you want to view?"
#fileline = raw_input("> ")

# this reads the next line, so it will only show the first if used this way
# the integer input tells it how many characters of that line to show
#print filename.readline(int(fileline))

#this rewrites filename using the input. only works if you add the "w" to the open function in line 2
changes = raw_input("What do you want to add? ")
print filename.write(changes)
