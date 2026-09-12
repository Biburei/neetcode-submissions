class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for index, val in enumerate(nums):
            pair = target - val

            if pair in seen:
                return [seen[pair], index]
            seen[val] = index