"""
this thing finds the lcm of number
"""


def scm(number):
    range_thing = 1
    while range_thing > -1:
        for i in range(number * range_thing, number * (range_thing + number), number):
            for j in range(2, number + 1):
                if divmod(i, j) == (i / j, 0):
                    if number == j and divmod(i, j) == (i / j, 0):
                        return i
                    else:
                        continue
                else:
                    break
        range_thing = range_thing + number


def main():
    number = input("smallest common multiple of numbers from 1 to what?")
    print scm(number)


if __name__ == '__main__':
    main()
