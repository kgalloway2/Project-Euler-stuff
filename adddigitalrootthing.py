import csv

def add(a,b):
    return a+b

def digroot(n):
    digit_list = []
    a = n
    for j in str(n):    
        digit_list.append(int(j))
    droot = reduce(add, digit_list, 0)
    while droot > 9:
        digit_list = []
        for j in str(droot):
            digit_list.append(int(j))
        droot = reduce(add, digit_list, 0)
    return [a, droot]

def digrootlist(n):
    root_list = []
    for i in range(1,n+1):
        root_list.append(digroot(i))
    return root_list

def file(n):
    f = open('adddigroot.csv', 'wb')
    with f:
        writer = csv.writer(f)
        for k in digrootlist(n):
            writer.writerow(k)

def main():
    number = input("Find digital roots up to which number?")
    
    file(number)

if __name__ == '__main__':
    main()