from sys import argv

script, filename = argv

print "Opening %r." % filename
txt = open(filename)

print txt.read()