class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while left < len(numbers):
            soma = numbers[left] + numbers[right] 
            if soma == target:
                return [left + 1, right + 1]
            if soma < target:
                left += 1
            elif soma > target:
                right -= 1