#Problem6:Pangram
#https://www.hackerrank.com/challenges/pangrams/problem
s = input().lower()
letters = set(ch for ch in s if ch.isalpha())
print("pangram" if len(letters) == 26 else "not pangram"
