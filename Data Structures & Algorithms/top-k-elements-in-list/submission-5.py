class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequent = {}
        # key: Number, value: Frequency of that number
        for num in nums:
            if num not in frequent:
                frequent[num] = 1
            else:
                frequent[num] += 1
        
        # How to sort so that we are getting the top k frequent
        sorted_items = sorted(frequent.items(), key = lambda item: item[1], reverse = True)[:k]
        topk = [item[0] for item in sorted_items]
        return topk
