#find prime factors of n
#find max of prime factors

def prime_factor(n):
	prime_factor_list = []
	for i in range(2,1000000):
		if divmod(n,i) == (n/i,0):
			prime_factor_list.append(i)
			n = n/i
		else:
			continue
	return prime_factor_list
	
def main():
	number = input("largest prime factor of what number?")
	print((prime_factor(number)))
	
if __name__ == '__main__':
	main()