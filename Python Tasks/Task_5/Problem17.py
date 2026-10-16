# Problem 17: No Idea!
# HackerRank: https://www.hackerrank.com/challenges/no-idea/problem
n, m = map(int, input().split())
array = list(map(int, input().split()))
liked = set(map(int, input().split()))
disliked = set(map(int, input().split()))

happiness = 0
for number in array:
    if number in liked:
        happiness += 1
    elif number in disliked:
        happiness -= 1

print(happiness)
