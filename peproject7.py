def nthprime(n):
    composite_list = []
    i = 2
    count = 0
    while count != n:
        if i not in composite_list:
            count += 1
            for j in range(i * i, n**2, i):
                composite_list.append(j)
        i += 1
    return i - 1

def nthprime2(n):

def main():
    number = input("nth prime, what is n?")
    print nthprime(number)


if __name__ == '__main__':
    main()
