print "This is a survey!"
print raw_input('What is your name?')
print raw_input('Favorite color?')
print '''I need to save this answer to print later.
So I set up the print a different way.'''
save_this = raw_input('What is your hair color?')

print "I saved %s, but not %s or %s." % (save_this, raw_input('What is your name?'), raw_input('Favorite color'))
