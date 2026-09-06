class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # what I did wrong was that I generated the anagrams in the list and check if it is in the input list, but if the word becomes really long, generating the anagrams will take too long and let alone finding it

        # What I should've done is that each word will have its own "signature" when sorted, for example, stop, pots, and tops all have opts signature when sorted out each letter in the word. We can put that into a hash map with the signature as keys and the values as the words
        group_anagrams = {}
        # How: First lets loop through the list
        for i in range(len(strs)):
            # We then want to take the word and sort it out alphabetically
            signature = ''.join(sorted(strs[i]))
            # this means that we are sorting the ith word in strs and then join them together
            # After that we are going to put this into a dictionary or hashmap where the signature is the key if it is not in the group anagram dictionary
            if signature not in group_anagrams:
                group_anagrams[signature] = []
            
            group_anagrams[signature].append(strs[i])
        
        # After that we are going to return the list of those values
        return list(group_anagrams.values())
