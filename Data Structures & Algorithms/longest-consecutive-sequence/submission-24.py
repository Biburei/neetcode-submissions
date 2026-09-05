class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums_set = set(nums)
        streak = 0
        max_streak = 0
        for x in nums_set:
            if (x-1) not in nums_set:
                current = x
                while (current) in nums_set:
                    streak += 1
                    current += 1
                if streak > max_streak:
                    max_streak = streak
            streak = 0
        return max_streak
        