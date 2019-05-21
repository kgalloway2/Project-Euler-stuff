def m35(n):
	m3_list = []
	m5_list = []
	for i in range(2,n):
		if i in range(3,n,3):
			m3_list.append(i)
	for i in range(2,n):
		if i in range(5,n,5):
			m5_list.append(i)
	return sum(m3_list)+sum(m5_list)

def main():
	number = input("sum multiples of 3 or 5 less than what?")
	print m35(number)
	
if __name__ == '__main__':
	main()