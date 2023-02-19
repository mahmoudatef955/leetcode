from __future__ import print_function

import re


def search_next_letter(letters, target):
    def next_greater_rec(start: int, end: int):
        if start > end:
            while letters[(end + 1) % len(letters)] == letters[end % len(letters)]:
                end = ((end + 1) % len(letters))

            return letters[(end + 1) % len(letters)]

        middle = (start + end) // 2

        if letters[middle] == target:
            while letters[(middle + 1) % len(letters)] == letters[middle % len(letters)]:
                middle = ((middle + 1) % len(letters))
            return letters[(middle + 1) % len(letters)]

        elif ord(letters[middle]) > ord(target):
            return next_greater_rec(start, middle - 1)
        else:
            return next_greater_rec(middle + 1, end)

    return next_greater_rec(0, len(letters) - 1)


class Solution:
    def reverseWords(self, s: str) -> str:
        words = re.sub(' +', ' ', s.strip()).split(' ')
        print(words)

        left_pointer = 0
        right_pinter = len(words) - 1

        while left_pointer < right_pinter:
            tmp = words[left_pointer]
            words[left_pointer] = words[right_pinter]
            words[right_pinter] = tmp

            left_pointer += 1
            right_pinter -= 1

        return " ".join(words)


def main():
    print(Solution().reverseWords("a good   example"))


if __name__ == "__main__":
    main()
