class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        d={' ':' '} #creates a blank dictionary
        c=97
        for i in range(len(key)):
            if key[i] not in d: #if key letter hasnt been seen yet
                d[key[i]]=chr(c) #map key letter to dictionary letter (english alphabet
                c+=1 #increment to next english alphabet letter

        result=''    
        for i in range(len(message)): #decode message
                result+=d[message[i]] 
        return result        
