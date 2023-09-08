class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        consistent = 0 #consistency counter

        for word in words: #increment through words list
            if all(char in allowed for char in word): #if one or more char is found in a string from words list, and only chars from allowed
                consistent += 1 #increment counter

        return consistent #return counter
