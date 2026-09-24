class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # First we need to get 2 pointers, one on the left and the other on the right
        left = 0
        right = len(nums) - 1
        if left == right:
            if nums[left] == target:
               return left
            else:
                return -1
        while (left < right):
            mid = left + (right - left) // 2
            if left + 1 == right:
                if nums[left] == target:
                    return left
                if nums[right] == target:
                    return right
                return -1
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid
            else:
                right = mid
        