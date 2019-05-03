numbers = []

def count(p,r):
    i = 0
    while i < p:
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + r
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

p = int(raw_input("Count to what?"))
r = int(raw_input("Count by what?"))
print count(p, r)

print "The numbers: "

for num in numbers:
    print num 