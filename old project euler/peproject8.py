def mult(a,b):
    return a*b

def list_from_numb(n):
    numblist = []
    for i in str(n):
        numblist.append(int(i))
    return numblist

def adjprod(n, d):
    product_list = []
    digit_list = []
    numb = list_from_numb(n)
    for i in range(len(numb)):
        new_product = reduce(mult, numb[i:i+d], 1)
        product_list.append(new_product)
        digit_list.append(numb[i:i+d])
        i += d-1
    max_product = product_list.index(max(product_list[:(len(numb)-d+1)]))
    return (product_list[max_product], digit_list[max_product])

def main():
    number = input("what number are we looking at?")
    digit = input("how many adjacent digits to make product?")
    print adjprod(number, int(digit))

if __name__ == '__main__':
    main()