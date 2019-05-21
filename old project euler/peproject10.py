def primesum(n):
    prime_list = [2]
    i = 3
    runningsum = 2
    while max(prime_list) < n:
        divisible = False
        for p in prime_list:
            if i%p == 0:
                divisible = True
                break 
        if not divisible:
            prime_list.append(i)
            runningsum = runningsum + i
        i +=1
    return runningsum - max(prime_list)

def main():
    number = input("sum of primes less than what?")
    print primesum(number)

if __name__ == '__main__':
    main()