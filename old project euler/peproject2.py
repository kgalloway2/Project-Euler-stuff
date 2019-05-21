def f(n):
	if n == 1: 
		return 1
	elif n == 2:
		return 1
	else:
		return f(n-1)+f(n-2)

def listf(n):
	listf = [] 
	for i in range(1, n):
		if f(i) < n:
			if divmod(f(i),2) == (f(i)/2,0) :
				listf.append(f(i))
			else:
				continue
		else:
			break
	return listf
	
def main():
	number = input("sum of even fibonaccis that do not exceed what?")
	print(listf(number))
	print(sum(listf(number)))

if __name__ == '__main__':
	main()