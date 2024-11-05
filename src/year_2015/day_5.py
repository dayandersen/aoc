from solver import AdventSolver
from collections import defaultdict


class Day5Solver(AdventSolver):
    VOWELS = {"a", "e", "i", "o", "u"}
    BANNED_BIGRAMS = {"ab", "cd", "pq", "xy"}
    """
    It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
    It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
    It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.

    """

    def part_1(self, input_data: list[str]) -> str:
        print(input_data)
        nice_words = 0
        for word in input_data[:-1]:
            is_nice = self.part_1_is_nice(word)
            # print(f"word: {word}, was {"NICE" if is_nice else "NAUGHTY"}")

            nice_words += 1 if is_nice else 0

        return str(nice_words)

    def part_1_is_nice(self, word: str) -> bool:
        vowel_count = 0
        contains_double = False
        naughty = False

        if len(word) < 3:
            return False

        if word[0] in self.VOWELS:
            vowel_count += 1
        if word[0] == word[1]:
            contains_double = True
        if word[0] + word[1] in self.BANNED_BIGRAMS:
            return False

        for i in range(1, len(word)):
            # Only count the first of the bigram so as to not overcount

            if word[i] in self.VOWELS:
                vowel_count += 1
            if word[i - 1] == word[i]:
                contains_double = True
            if word[i - 1] + word[i] in self.BANNED_BIGRAMS:
                return False
        vowel_count += 1 if word[-1] in self.VOWELS and len(word) % 2 != 0 else 0
        # print(f"vowel_count: {vowel_count}, contains_double: {contains_double}")
        return True if vowel_count >= 3 and contains_double else False

    def part_2(self, input_data: list[str]) -> str:
        nice_words = 0
        for word in input_data[:-1]:
            is_nice = self.part_2_is_nice(word)
            print(f"word: {word}, was {"NICE" if is_nice else "NAUGHTY"}")

            nice_words += 1 if is_nice else 0

        return str(nice_words)

    def part_2_is_nice(self, word: str) -> bool:
        if len(word) < 4:
            return False
        bigram_counts: defaultdict = defaultdict(lambda: 0)
        contains_repeating_pair = False
        contains_sandwhich = False
        repeat_count = False

        bigram_counts[word[-2] + word[-1]] += 1

        for i in range(len(word) - 1):
            bigram = word[i : i + 2]
            if bigram in word[i + 2 :]:
                contains_repeating_pair = True
                break
        else:
            contains_repeating_pair = False

        for i in range(1, len(word) - 1):
            if word[i - 1] == word[i + 1]:
                contains_sandwhich = True

        return contains_sandwhich and contains_repeating_pair
