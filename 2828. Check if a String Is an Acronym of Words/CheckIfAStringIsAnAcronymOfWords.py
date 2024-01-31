class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        output = False #output var
        acro = "" #temp var

        for each in words: #for loop to place first letter of each word in temp var
            if each[0]:
                acro += each[0]

        if acro == s: #if temp var and acronym string are equal, return true, else false
            output = True
        else:
            output = False
    
        return output #return output
