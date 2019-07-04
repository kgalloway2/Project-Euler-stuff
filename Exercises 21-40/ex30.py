# lines 2-4 define variables
people = 30
cars = 40
buses = 15

# the next line are a bunch of if statements
# the first gives a condition, and if true, it will do the action below it
# the next line (elif) gives an alternate condition
# if the first condition is not met, it checks the elif condition 
# if true, it runs the elif code
# if neither if nore elif are true, it does the else condition
if cars > people:
    print "We shoud take the cars."
elif cars < people:
    print "We should not take the cars."
else: 
    print "We can't decide."

# same as 6-11
if buses > cars:
    print "That's too many buses."
elif buses < cars:
    print "Maybe we should take the buses."
else:
    print "We still can't decide."

# same as 6-11
if people > buses:
    print "Alright, let's just take the buses."
else:
    print "Fine, let's stay home then."

# same as 6-11
if cars > buses and people > buses:
    print "Yes."
else:
    print "Nope."