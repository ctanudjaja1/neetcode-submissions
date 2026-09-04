class Solution:
    def get_anagrams(self, word):

        # Base case: if the word has 1 or 0 characters
        if len(word) <= 1:
            return [word]

        all_anagrams = []

        # Iterate through each character in the word
        for i in range(len(word)):
            current_char = word[i]
            remaining_chars = word[:i] + word[i + 1 :]

            # Recursively get anagrams of the remaining characters
            for sub_anagram in self.get_anagrams(remaining_chars):
                all_anagrams.append(current_char + sub_anagram)
        
        return all_anagrams
        

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Group Anagrams is where you can make the same exact characters as another string
        # Thoughts on how to approach it, I think what we need to do is check the letters with the string because anagrams contains the same letters just arrange differently
        # I think what we can do is take each word put it into a hashmap, and sort the letters in the words and put each it as a value to the word as a key. And so if value is in the key put them together

        groups = []
        # Keep track of words we've already grouped so we don't process them twice
        visited = set()
        
        for i in range(len(strs)):
            if strs[i] in visited:
                continue
                
            # Generate ALL possible variations of this word
            # Convert to a set for instant O(1) lookups
            possible_permutations = set(self.get_anagrams(strs[i]))
            
            current_group = []
            
            # Look through the rest of the list to see if any match the permutations
            for word in strs:
                if word in possible_permutations:
                    current_group.append(word)
                    visited.add(word)
                    
            groups.append(current_group)
            
        return groups

        