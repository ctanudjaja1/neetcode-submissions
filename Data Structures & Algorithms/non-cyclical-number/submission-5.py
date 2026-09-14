class Solution:
    def __init__(self):
        self.number_seen = []
    
    def isHappy(self, n: int) -> bool:

        res = 0
        for d in str(abs(n)):
            res += int(d) ** 2

        if res == 1:
            return True
        
        if res in self.number_seen:
            return False
        
        self.number_seen.append(res)
        return self.isHappy(res)            
        
        