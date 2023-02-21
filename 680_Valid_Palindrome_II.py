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
