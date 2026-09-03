class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq = {}

        # Step 1: initialize counts (like your 0 idea, but increment)
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        # Step 2: process second string
        for ch in t:
            if ch not in freq:
                return False
            
            freq[ch] -= 1

            if freq[ch] < 0:
                return False

        # Step 3: check all zero
        return all(value == 0 for value in freq.values())