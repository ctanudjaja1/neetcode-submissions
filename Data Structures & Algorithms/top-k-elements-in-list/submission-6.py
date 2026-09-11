class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequent = {}
        # key: Number, value: Frequency of that number
        # O(n)
        for num in nums:
            if num not in frequent:
                frequent[num] = 1
            else:
                frequent[num] += 1
        
        # How to sort so that we are getting the top k frequent
        # O(n log n)
        sorted_items = sorted(frequent.items(), key = lambda item: item[1], reverse = True)[:k]
        # O(n)
        topk = [item[0] for item in sorted_items]

        # Time and space
        # Time: O(n log n)
        # Space: O(n)
        return topk
