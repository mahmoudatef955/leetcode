import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]+', '', s).lower()
        pointer1 = 0
        pointer2 = len(s) - 1

        while pointer2 > pointer1:

            if s[pointer1] != s[pointer2]:
                return False

            pointer1 += 1
            pointer2 -= 1

        return True
