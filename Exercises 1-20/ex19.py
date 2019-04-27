# this defines the cheese and crackers function to print out all these statements,
# filing some with inputs from the function
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"

# this shows one way to give the function an input
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

# this shows a way to define variables and then use them as inputs for the function
print "OR, we can use variable from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# this shows another way to provide inputs, doing math
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

# this shows another way to define inputs, combining the two previous ways 
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000) 