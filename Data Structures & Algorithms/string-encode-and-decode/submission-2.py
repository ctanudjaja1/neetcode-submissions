class Solution: 
    def encode(self, strs: List[str]) -> str:
        encoded_string = ''
        for s in strs:
            encoded_string += str(len(s)) + '#' + s
        print(encoded_string)
        return encoded_string

    def decode(self, s: str) -> List[str]:
        # Given how it is the length after the # we need to count the number after the #
        decoded_string = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            
            length = int(s[i:j])
            word = s[j + 1 : j + 1 + length]
            decoded_string.append(word)
            i = j + 1 + length
            
        return decoded_string
