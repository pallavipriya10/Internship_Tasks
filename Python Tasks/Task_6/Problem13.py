#Problem13:Set-Union
#https://www.hackerrank.com/challenges/py-set-union/problem
n = int(input())
english = set(input().split())
m = int(input())
french = set(input().split())
print(len(english | french))
