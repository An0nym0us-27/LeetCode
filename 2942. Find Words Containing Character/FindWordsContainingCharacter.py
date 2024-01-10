class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        
        found = [] #create a list

        for index in range(len(words)): #go through the list of words
            if x in words[index]: #if the char is found in a word
                found.append(index) #add that index to our found list

        return found #return result
