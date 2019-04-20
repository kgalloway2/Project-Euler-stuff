import csv

def rev(n):
	a = 0
	while n > 0:
		a = (a*10)+(n%10)
		n = n/10
	return a

def balln(n):
    ball_list = []
    count = 1
    while len(ball_list) < n:
        a = count
        b = rev(a)
        c = a*b
        if c == rev(c):
            ball_list.append([a,b,c])
        count +=1
    return ball_list

def file(n):
    f = open('ballnumbers.csv', 'wb')
    with f:
        writer = csv.writer(f)
        for k in balln(n):
            writer.writerow(k)

def main():
	number = input("How many ball numbers should I find?")
	file(number)
    
if __name__ == '__main__':
	main()