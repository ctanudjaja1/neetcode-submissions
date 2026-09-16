class Solution:
    def isPalindrome(self, s: str) -> bool:
        # since tht it is case-insensitive, we want to join them together and make them all lowercase, then we are going to put 2 pointers at the start and end of the array, then we are going to double check
        s = s.replace(" ", "")
        result = s.lower()
        left, right = 0, len(result) - 1
        while left < right:
            if not result[left].isalnum():
                left += 1
                continue
            if not result[right].isalnum():
                right -= 1
                continue
            if result[left] != result[right]:
                return False
            else:
                left += 1
                right -= 1
        
        return True