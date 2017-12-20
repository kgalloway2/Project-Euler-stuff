
def product_list(n):
	product_list = []
	for i in range(1,10**n):
		for j in range(1,10**n):
			if i*j in product_list:
				continue
			else:
				product_list.append(i*j)
	return product_list

def rev(n):
	a = 0
	while n > 0:
		a = (a*10)+(n%10)
		n = n/10
	return a
	
def palindrome(n):
	palindrome_list = []
	for b in product_list(n):
		if rev(b) == b: 
			palindrome_list.append(b)
		else:
			continue
	return palindrome_list
	
def main():
	number = input("largest palindromic product of how many digit numbers?")
	print(palindrome(number))

if __name__ == '__main__':
	main()