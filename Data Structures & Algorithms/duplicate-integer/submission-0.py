class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen = set()
        for nums in nums:
            if nums in seen:
                return True
            seen.add(nums)
        return False
        # This have an O(n) space and O(n) time complexity