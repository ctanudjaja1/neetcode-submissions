"""
Given an integer array nums, 
input is nums
output is the array of the product of all elements except the current

return an array output where output[i] is the product of all the elements of nums except nums[i].

Step 1: get all elements
step 2: divide it by the current element
step 3: add it to a hashmap

Each product is guaranteed to fit in a 32-bit integer. 
"""


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, zero_cnt = 1, 0
        for num in nums:
            if num:
                prod *= num
            else:
                zero_cnt +=  1
        if zero_cnt > 1: return [0] * len(nums)

        res = [0] * len(nums)
        for i, c in enumerate(nums):
            if zero_cnt: res[i] = 0 if c else prod
            else: res[i] = prod // c
        return res
                
            

        
        