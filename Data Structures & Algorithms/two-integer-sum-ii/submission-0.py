class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low = 0
        high = len(numbers) - 1
        while low < high:
            current_number = numbers[low] + numbers[high]
            if current_number == target:
                return [low + 1, high + 1]
            if current_number < target:
                low += 1
                continue
            if current_number > target:
                high -= 1
                continue
            
