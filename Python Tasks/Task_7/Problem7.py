#Problem7:Alphabet-Rangoli
#https://www.hackerrank.com/challenges/alphabet-rangoli/problem
def print_rangoli(size):
    width = 4 * (size - 1) + 1
    a_ord = ord("a")
    upper_rows = []
    for i in range(1, size + 1):
        start = a_ord + size - 1
        stop = a_ord + size - i - 1
        step = -1
        left = [chr(j) for j in range(start, stop, step)]
        right = left[-2::-1]
        upper_rows.append(("-".join(left + right)).center(width, "-"))

    lower_rows = upper_rows[-2::-1]
    print("\n".join(upper_rows + lower_rows))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

