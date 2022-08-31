class Solution:
    def isPalindrome(self, x: int) -> bool:
        num_str = str(x)
        pointer1, pointer2 = 0, len(num_str) - 1
        while pointer1 <= pointer2:
            if num_str[pointer1] != num_str[pointer2]:
                return False
            pointer1 += 1
            pointer2 -= 1
        return True
