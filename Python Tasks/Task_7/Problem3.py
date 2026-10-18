#Problem3:Mars Exploration
#https://www.hackerrank.com/challenges/mars-exploration/problem
s = input().strip()
expected = "SOS"
changed = 0
for i, char in enumerate(s):
    if char != expected[i % 3]:
        changed += 1
print(changed)
