def primes(n):
    prime_list = [2]
    i = 3
    count = 1
    while i < n:
        divisible = False
        for p in prime_list:
            if i%p == 0:
                divisible = True
                break 
        if not divisible:
            prime_list.append(i)
            count +=1
        i +=1
    return prime_list

def main():
    number = input("list of primes up to what number?")
    print primes(number)


if __name__ == '__main__':
    main()
