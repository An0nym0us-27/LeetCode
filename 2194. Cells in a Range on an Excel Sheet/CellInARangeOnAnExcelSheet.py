#This is not my code. Use to study
class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        res = [] #result
        for ch in range(ord(s[0]), ord(s[3])+1): #checks unicode letters inbetween start and end cell column letters
            for i in range(int(s[1]), int(s[4])+1): #checks numbers in range of start and end row
                res.append(f'{chr(ch)}{i}') #combines column and rows and appends them to list
        return res#return result
