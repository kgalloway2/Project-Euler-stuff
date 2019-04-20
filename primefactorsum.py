import csv

def prime_factor(n):
    prime_factor_list = []
    d = 2
    while n > 1:
        if divmod(n,d) == (n/d,0):
            prime_factor_list.append(d)
            n=n/d
        else:
            d+=1
    return prime_factor_list

def sum_of_factors(n):
    return sum(prime_factor(n))

def continued_sum(n):
    c = 1
    ogn = 2
    sum_list = []
    while n > c:
        if ogn == sum_of_factors(ogn):
            sum_list.append([c+1,sum_of_factors(ogn)])
            c = c+1
            ogn = c+1
        else:
            ogn = sum_of_factors(ogn)
    return sum_list

def file(n):
    f = open('continuedsum.csv', 'wb')
    with f:
        writer = csv.writer(f)
        for k in continued_sum(n):
            writer.writerow(k)

def main():
    number = input("sum of prime factors of n?")
    file(number)
	
if __name__ == '__main__':
	main()