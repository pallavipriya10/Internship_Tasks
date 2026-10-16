# Problem 20: Piling Up!
# HackerRank: https://www.hackerrank.com/challenges/piling-up/problem
for _ in range(int(input())):
    n = int(input())
    blocks = list(map(int, input().split()))

    left = 0
    right = n - 1
    last = float("inf")
    possible = True

    while left <= right:
        if blocks[left] >= blocks[right]:
            chosen = blocks[left]
            left += 1
        else:
            chosen = blocks[right]
            right -= 1

        if chosen > last:
            possible = False
            break
        last = chosen

    print("Yes" if possible else "No")
