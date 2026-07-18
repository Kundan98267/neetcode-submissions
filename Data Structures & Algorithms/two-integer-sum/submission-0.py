class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1

        seen = {}

        for idx, num in enumerate(nums):
            diff = target - num

            if diff in seen:
                return [seen[diff],idx]

            seen[num] = idx
