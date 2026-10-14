"""Task 3: Python Coding & Problem-Solving
Reusable functions for Questions 1–15.
"""

from collections import Counter


# Q1. Find the Frequency of Each Word in a Sentence
def word_frequency(sentence):
    """Return a dictionary containing the frequency of each word."""
    frequencies = {}
    for word in sentence.split():
        frequencies[word] = frequencies.get(word, 0) + 1
    return frequencies


# Q2. Find the Frequency of Each Character in a Word
def character_frequency(word):
    """Return a dictionary containing the frequency of each character."""
    frequencies = {}
    for char in word:
        frequencies[char] = frequencies.get(char, 0) + 1
    return frequencies


# Q3. Find the First Non-Repeating Character in a Word
def first_non_repeating_character(word):
    """Return the first character occurring once, or None if there is none."""
    frequencies = Counter(word)
    for char in word:
        if frequencies[char] == 1:
            return char
    return None


# Q4. Check Whether Two Strings Are Anagrams
def are_anagrams(s1, s2):
    """Return True if strings contain the same characters with the same frequencies."""
    return Counter(s1) == Counter(s2)


# Q5. Find the First Repeating Character in a String
def first_repeating_character(text):
    """Return the character whose second occurrence is first encountered, else None."""
    seen = set()
    for char in text:
        if char in seen:
            return char
        seen.add(char)
    return None


# Q6. Move All Zeros to the End of a List
def move_zeros_to_end(nums):
    """Return a new list with non-zero values in order, followed by all zeros."""
    non_zeros = [num for num in nums if num != 0]
    zeros = [num for num in nums if num == 0]
    return non_zeros + zeros


# Q7. Find the Second Highest Distinct Number in a List
def second_highest_distinct(nums):
    """Return the second-largest distinct number, or None if it does not exist."""
    unique_nums = sorted(set(nums), reverse=True)
    return unique_nums[1] if len(unique_nums) >= 2 else None


# Q8. Remove Duplicates Without Changing the Original Order
def remove_duplicates_preserve_order(nums):
    """Return a list of unique values in order of first appearance."""
    result = []
    seen = set()
    for num in nums:
        if num not in seen:
            result.append(num)
            seen.add(num)
    return result


# Q9. Find the Missing Number from 1 to N
def find_missing_number(nums, n):
    """Return the missing number from 1..n, assuming exactly one is missing."""
    expected_sum = n * (n + 1) // 2
    return expected_sum - sum(nums)


# Q10. Find Two Numbers Whose Sum Equals a Target
def first_pair_sum(nums, target):
    """Return the first qualifying pair by earliest second element, or []."""
    seen = []
    for num in nums:
        complement = target - num
        if complement in seen:
            # The first matching earlier value is the earliest qualifying value.
            for earlier in seen:
                if earlier == complement:
                    return [earlier, num]
        seen.append(num)
    return []


# Q11. Find the Number Closest to Zero
def closest_to_zero(nums):
    """Return the value closest to zero; choose positive on an equal-distance tie."""
    if not nums:
        return None
    return min(nums, key=lambda num: (abs(num), num < 0))


# Q12. Find Common Elements Between Two Lists
def common_elements(list1, list2):
    """Return unique common elements in order of first occurrence in list1."""
    second = set(list2)
    result = []
    seen = set()
    for value in list1:
        if value in second and value not in seen:
            result.append(value)
            seen.add(value)
    return result


# Q13. Rotate a List to the Right by K Positions
def rotate_right(nums, k):
    """Return a new list rotated right by k positions."""
    if not nums:
        return []
    k %= len(nums)
    return nums[-k:] + nums[:-k] if k else nums[:]


# Q14. Find the Maximum Sum of Two Consecutive Elements
def max_consecutive_pair_sum(nums):
    """Return the maximum sum of adjacent elements; input must have >= 2 values."""
    if len(nums) < 2:
        raise ValueError("At least two elements are required.")
    return max(nums[i] + nums[i + 1] for i in range(len(nums) - 1))


# Q15. Find All Pairs of Numbers Whose Sum Equals a Target
def all_unique_pairs_sum(nums, target):
    """Return unique ascending pairs, sorted by each pair's first element."""
    pairs = set()
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                pairs.add(tuple(sorted((nums[i], nums[j]))))
    return [list(pair) for pair in sorted(pairs)]
