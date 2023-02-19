import re


class Solution:
    def reverseWords(self, s: str) -> str:
        words = re.sub(' +', ' ', s.strip()).split(' ')

        left_pointer = 0
        right_pinter = len(words) - 1

        while left_pointer < right_pinter:
            tmp = words[left_pointer]
            words[left_pointer] = words[right_pinter]
            words[right_pinter] = tmp

            left_pointer += 1
            right_pinter -= 1

        return " ".join(words)
