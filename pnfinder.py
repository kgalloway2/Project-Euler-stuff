def factor_list(i) :
	factor_list = [1]
	for j in range(2, (i/2)+1):
		if divmod(i,j) == (i/j,0):
			factor_list.append(j)
	return factor_list
	
def pn_finder(n) :
	pn_list = []
	for i in range(2,n+1):
		if sum(factor_list(i)) == i:
			pn_list.append(i)	
	return pn_list

def main():
	print("find perfect numbers less than n.")
	number = input("what is n?")
	print(pn_finder(number))
	
if __name__ == '__main__':
	main() 