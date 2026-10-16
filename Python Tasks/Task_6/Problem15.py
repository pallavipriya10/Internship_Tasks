#Problem15:set-difference()
#https://www.hackerrank.com/challenges/py-set-difference-operation/problem
n = int(input())
english = set(input().split())
m = int(input())
french = set(input().split())
print(len(english - french)
