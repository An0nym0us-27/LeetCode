#This is NOT my code, used for learning purposes

class Solution:
    def similarPairs(self, words: List[str]) -> int:
        counter = 0

        for strings in range(len(words)): #looped through strings
            for letter in range(strings): #looped through letters
                if set(words[strings]) == set(words[letter]): #if letters from the sets matched, increment counter (since sets must contain unique values)
                    counter +=1
            
        return counter #return result
