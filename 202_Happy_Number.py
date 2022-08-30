class Solution:
    def isHappy(self, num: int) -> bool:
        if num == 1:
            return True
        slow, fast = num, num

        fast_digits = [int(d) for d in str(fast)]
        fast = sum(n * n for n in fast_digits)
        while slow != fast:
            slow_digits = [int(d) for d in str(slow)]
            slow = sum(n * n for n in slow_digits)

            fast_digits = [int(d) for d in str(fast)]
            fast = sum(n * n for n in fast_digits)

            if fast == 1:
                return True
            fast_digits = [int(d) for d in str(fast)]
            fast = sum(n * n for n in fast_digits)

            if fast == 1:
                return True

        return False
