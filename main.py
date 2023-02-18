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
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]+', '', s).lower()
        pointer1 = 0
        pointer2 = len(s) - 1

        print(s)
        while pointer2 > pointer1:

            if s[pointer1] != s[pointer2]:
                return False

            pointer1 += 1
            pointer2 -= 1

        return True


def main():
    # print(search_next_letter(['a', 'c', 'f', 'h'], 'f'))
    # print(search_next_letter(['a', 'c', 'f', 'h'], 'h'))
    # print(search_next_letter(['a', 'c', 'f', 'h'], 'm'))
    # print(search_next_letter(["e", "e", "g", "g"], 'g'))
    print(Solution().isPalindrome("ab_a"))


if __name__ == "__main__":
    main()
