from sys import argv

script, start_year, end_year = argv

def leaps(start, end):
    leap_years = 0
    for i in xrange(long(start), long(end), 4):
        leap_year = False
        if i % 4 == 0:
            if i % 100 == 0:
                if ((i % 900) == 200) or ((i % 900) == 600):
                    leap_year = True
                else:
                    pass
            else:
                leap_year = True
        else:
            pass
        if leap_year == True:
            leap_years += 1
    return leap_years

if (long(start_year) % 4) != 0:
    print leaps(long(start_year) + (4 - (long(start_year) % 4)), long(end_year))
else:
    print leaps(long(start_year), long(end_year))