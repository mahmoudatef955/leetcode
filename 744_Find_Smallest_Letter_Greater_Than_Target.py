class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:

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
