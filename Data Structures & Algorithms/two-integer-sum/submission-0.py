class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Lets brute force it
        # Thought: I'm going to do 2 loops through the array where i != j meaning that I want one start on the beginning and the other start on the end where I will pick the number and added
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    value = nums[i] + nums[j]
                    if value == target:
                        return [i, j]
