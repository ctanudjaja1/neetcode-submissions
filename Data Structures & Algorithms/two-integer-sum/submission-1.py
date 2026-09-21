class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # One-pass Hashmap solution
        visited = {}
        for i in range(len(nums)):
            dif = target - nums[i]                
            if dif in visited:
                return [visited[dif], i]
            visited[nums[i]] = i 
