"""Run sample inputs and additional test cases for all 15 questions."""

from solutions import (
    word_frequency, character_frequency, first_non_repeating_character,
    are_anagrams, first_repeating_character, move_zeros_to_end,
    second_highest_distinct, remove_duplicates_preserve_order,
    find_missing_number, first_pair_sum, closest_to_zero, common_elements,
    rotate_right, max_consecutive_pair_sum, all_unique_pairs_sum
)


def run_tests():
    print("Q1 Sample:", word_frequency("python is easy and python is powerful"))
    print("Q1 Additional:", word_frequency("red blue red"))
    print("Q2 Sample:", character_frequency("banana"))
    print("Q2 Additional:", character_frequency("book"))
    print("Q3 Sample:", first_non_repeating_character("swiss"))
    print("Q3 Additional:", first_non_repeating_character("aabb"))
    print("Q4 Sample:", are_anagrams("listen", "silent"))
    print("Q4 Additional:", are_anagrams("hello", "world"))
    print("Q5 Sample:", first_repeating_character("programming"))
    print("Q5 Additional:", first_repeating_character("abc"))
    print("Q6 Sample:", move_zeros_to_end([0, 3, 0, 1, 2, 0, 4]))
    print("Q6 Additional:", move_zeros_to_end([1, 0, 2]))
    print("Q7 Sample:", second_highest_distinct([10, 20, 40, 30, 40, 20]))
    print("Q7 Additional:", second_highest_distinct([5, 5]))
    print("Q8 Sample:", remove_duplicates_preserve_order([4, 2, 4, 5, 2, 7, 5]))
    print("Q8 Additional:", remove_duplicates_preserve_order([1, 1, 2]))
    print("Q9 Sample:", find_missing_number([1, 2, 4, 5, 6], 6))
    print("Q9 Additional:", find_missing_number([1, 3, 4], 4))
    print("Q10 Sample:", first_pair_sum([2, 7, 11, 15], 9))
    print("Q10 Additional:", first_pair_sum([1, 4, 2, 3], 6))
    print("Q11 Sample:", closest_to_zero([-8, -3, 2, 5, -2]))
    print("Q11 Additional:", closest_to_zero([-1, 1, 4]))
    print("Q12 Sample:", common_elements([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]))
    print("Q12 Additional:", common_elements([2, 2, 3], [2, 3, 3]))
    print("Q13 Sample:", rotate_right([1, 2, 3, 4, 5], 2))
    print("Q13 Additional:", rotate_right([1, 2, 3], 0))
    print("Q14 Sample:", max_consecutive_pair_sum([4, 7, 2, 9, 5]))
    print("Q14 Additional:", max_consecutive_pair_sum([-5, -2, -7]))
    print("Q15 Sample:", all_unique_pairs_sum([2, 4, 3, 5, 7, 8, 1], 9))
    print("Q15 Additional:", all_unique_pairs_sum([1, 1, 2, 3, 4], 5))


if __name__ == "__main__":
    run_tests()
