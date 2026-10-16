#Problem14:Set-intersection
#https://www.hackerrank.com/challenges/py-set-intersection-operation/problem
n = int(input())
english = set(input().split())
m = int(input())
french = set(input().split())
print(len(english & french))
