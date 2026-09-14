class Solution:
    def __init__(self):
        self.number_seen = []

    def isHappy(self, n):
        sum = 0

        for d in str(abs(n)):
            sum += int(d) ** 2

        if sum == 1:
            return True

        if sum in self.number_seen:
            return False

        self.number_seen.append(sum)

        return self.isHappy(sum)         
        
        