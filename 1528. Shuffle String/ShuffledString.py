class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:

        myDict = {} #create hashmap
        j = 0 #integer var
        
        for i in indices: #add letters from to string to hashmap by linking them to the indices values
            myDict[i] = s[j]
            j += 1 #to increment to next index in indices

        updated = dict(sorted(myDict.items())) #sort hash map by key
        shuffled = ''.join (str(values) for values in updated.values()) #join hashmap values into a string

        return shuffled #return output
