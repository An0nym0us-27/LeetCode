class Solution:
    def finalString(self, s: str) -> str:
        output = "" #output string
        for i in s:
            if i == "i": #if an "i" is detected, remove it and reverse all in string
                output.replace("i", "")
                output = output[::-1]
            else: #else, continue adding to string
                output += i
        
        return output #return output
