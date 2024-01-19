class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        
        w1 = "" #word1 string var
        w2 = "" #word2 string var
        result = False #boolean result var

        for char in word1:
            w1 += char #add from list to string
        for char in word2:
            w2 += char #add from list to string

        if w1.join(w1) == w2.join(w2): #join each letter in respective strings so that it is easier to compare, if equal result is changed to true
            result = True 
        else:
            result = False #else is false

        return result #return result
