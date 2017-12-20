def factor_list(i) :
	factor_list = []
	for j in range(1, i):
		if divmod(i,j) == (i/j,0):
			factor_list.append(j)
	return factor_list
	
def pn_finder(n) :
	pn_list = []
	for i in range(1,n+1):
		if sum(factor_list(i)) == i:
			pn_list.append(i)	
	return pn_list

def main():
	print("find perfect numbers less than n.")
	number = input("what is n?")
	print(pn_finder(number))
	
if __name__ == '__main__':
	main() 