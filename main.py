from __future__ import print_function


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
    def validPalindromeNormal(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        deleted_char_count = 0

        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1

            else:
                return self.validPalindromeNormal(s[left + 1:right + 1]) or self.validPalindromeNormal(s[left:right])

        return True


def main():
    # print(Solution().validPalindrome(
    #     "ebcbbececabbacecbbcbe"))
    # print(Solution().validPalindrome(
    #     "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"))

    print(Solution().validPalindrome(
        "aba"))


if __name__ == "__main__":
    main()

# cupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupucu
