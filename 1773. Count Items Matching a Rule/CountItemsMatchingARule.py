class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        x = 0
        cntr = 0 #counter result var
        if ruleKey == "type": #set x to corresponding index for corresponding ruleKey
            x = 0
        elif ruleKey == "color":
            x = 1
        elif ruleKey == "name":
            x = 2

        for i in items:
            for each in range(len(i)): #loop through each list
                if each == x and i[each] == ruleValue: #if string equals correct ruleKey and ruleValue
                    cntr += 1 #increment counter by 1
                else:
                    pass
        return cntr #return counter
