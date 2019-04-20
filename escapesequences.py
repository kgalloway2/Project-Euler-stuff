backslash = "I use the \\ backslash \\."
single_quote = "I use the \'single-quote\'."
double_quote = "I use the \"douhbe-quote\"."
bell = "I use the \a ASCII bell \a \a \a."
backspace = "I use the \b ASCII backspace \b."
formfeed = "I use the \f ASCII formfeed \f \f."
linefeed = "I use the \nASCII llinefeed.\nThis starts a new line."
character = "I can print characters like \N{pi}."
carraige_return = "I do carraige returns like this. \rDo you see\rit?"
tab = "What \tdo \tyou \tthink I \tdo?"
hexval16 = "I do things with 16-bit numbers \u1276."
hexval32 = "Me too but with 32 \U17353799."
vertical_tab = "\vWhat is a \vvertival \vtab?"
octal = "I do octal numbers \023."
hexvalue = "I do hex as well \x38."

# let's try the thing from the book
#while True: 
 #   for i in ["/","-","|","\\","|"]:
  #      print "%s\r" % i,

print """"
We in the \nBIG LEAUGES\n\tnow.
I am combining\\escape sequences\\
\twith %s,
Even with %r.
""" % ('formatted variables', 'formatted variables')

print '''
Let's do something %s.
Use the escape sequences inside the %s. 
Does it still %r
''' % ('\\different\\', '\nformatted variables', '\'work?\'')
