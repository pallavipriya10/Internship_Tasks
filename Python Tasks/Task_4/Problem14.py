#Problem14:Count the number of distinct country names.
#https://www.hackerrank.com/challenges/py-set-add/problem
if __name__ == '__main__':
    n = int(input())
    countries = set()

    for _ in range(n):
        countries.add(input().strip())

    print(len(countries))

