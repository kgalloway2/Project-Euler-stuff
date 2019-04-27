# this defines formatter as a sting of 4 input variables
formatter = "%r %r %r %r"

# each of these print the variable 'formatter' filling in the four variables with the four inputs from the following list
print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)