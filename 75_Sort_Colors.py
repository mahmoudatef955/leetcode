class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return nums

        left = 0
        right = 1
        for current_color in range(3):
            while right < len(nums):
                if nums[left] == current_color:
                    left += 1
                    right = left + 1
                elif nums[right] == current_color:
                    tmp = nums[left]
                    nums[left] = nums[right]
                    nums[right] = tmp
                    left += 1
                    right = left + 1
                else:
                    right += 1
            right = left + 1

        return nums
