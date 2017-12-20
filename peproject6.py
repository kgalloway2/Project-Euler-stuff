def sumofsquares(n):
    squares_list = []
    for i in range(1, n + 1):
        squares_list.append(i**2)
    return sum(squares_list)


def squareofsum(n):
    list1 = []
    for i in range(1, n + 1):
        list1.append(i)
    a = sum(list1)
    return a**2


def main():
    number = input(
        "difference of sum of squares and square of sum up to what number?")
    print abs(sumofsquares(number) - squareofsum(number))


if __name__ == '__main__':
    main()
