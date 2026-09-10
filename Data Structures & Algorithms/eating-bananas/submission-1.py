class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h == len(piles):
            return max(piles)
        left = 1
        right = max(piles)
        min_speed = 0

        while left < right:
            mid = (left + right) // 2
            hours = 0

            for pile in piles:
                hours += (pile + mid - 1) // mid
            if hours > h:
                left = mid + 1
            elif hours <= h:
                right = mid
        return left
