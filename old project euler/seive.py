def seive_of_eratosthenes(n):
    composite_list = []  # Create list of composites (initially empty)
    prime_list = []  # Create list of primes (initially empty)
    # cycle through numbers from 2 to n (bound is exclusive)
    for i in range(2, n+1):
        # if i is not in the list of composites
        if i not in composite_list:
            # it is a prime, add it to the correct list
            prime_list.append(i)
            # cycle through numbers from i*i to n in steps of i
            for j in range(i*i, n+1, i):
                # add these numbers to composites
                composite_list.append(j)
    # return the list of primes.
    return prime_list


def main():
    # print out info
    print("Seive of Eratosthenes: Returns list of primes up to n.")
    # take an integer input from the user
    number = input("What is n? ")
    # run the seive and print the resulting list
    print(seive_of_eratosthenes(number))

# this runs the main() function if this file is executed
if __name__ == '__main__':
    main()
