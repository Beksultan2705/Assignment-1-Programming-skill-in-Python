from collections import Counter

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        char_count = Counter(s)
      
        # Iterate through each character in string 't'
        for char in t:
            # Decrement the count for the current character
            char_count[char] -= 1
          
            # If count becomes less than zero, it means this character is the extra one
            if char_count[char] < 0:
                return char
      
        # The function assumes that it is guaranteed there is an answer
        # If all characters match, this line would theoretically not be reached
