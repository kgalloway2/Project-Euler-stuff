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
    prime_list = [2]
    i = 3
    count = 1
    while count != n:
        divisible = False
        for p in prime_list:
            if i%p == 0:
                divisible = True
                break 
        if not divisible:
            prime_list.append(i)
            count +=1
        i +=1
    return prime_list[len(prime_list)-1]

def main():
    number = input("nth prime, what is n?")
    print nthprime2(number)


if __name__ == '__main__':
    main()
