class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Understand: We are given an array and an integer k and we are returning the k most frequent element.
        # For example:

        # If we have: [1, 1, 1, 2, 2, 3] and k = 2, it will return [1,2] since that 1 is the most frequent element and 2 is the 2nd most frequent element

        # Thoughts: First thing we need to do is to sort the array
        nums.sort()

        # After that we need to have a counter and iterate through array and if the value changes we will change the counter
        frequency = 1
        prev_val = nums[0] 
        frequent = {}
        for i in nums[1:]:
            if i != prev_val:
                # if the previous value doesn't equal to the current value we are going to add that to the dictionary where the key will be the value in the nums array and the frequency will be the value of the dictionary
                frequent[prev_val] = frequency

                frequency = 1
                prev_val = i
            else:
                frequency += 1
        frequent[prev_val] = frequency
        
        sorted_keys = sorted(frequent.keys(), key=lambda x: frequent[x], reverse=True)
        return sorted_keys[:k]