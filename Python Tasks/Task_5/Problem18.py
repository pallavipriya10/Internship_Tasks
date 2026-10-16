# Problem 18: The Minion Game
# HackerRank: https://www.hackerrank.com/challenges/the-minion-game/problem
def minion_game(string):
    vowels = "AEIOU"
    kevin = 0
    stuart = 0
    n = len(string)

    for i, char in enumerate(string):
        points = n - i
        if char in vowels:
            kevin += points
        else:
            stuart += points

    if kevin > stuart:
        print("Kevin", kevin)
    elif stuart > kevin:
        print("Stuart", stuart)
    else:
        print("Draw")

if __name__ == "__main__":
    s = input().strip()
    minion_game(s)
