class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        spaces = 0 #space counter
        updatedString = [] #updated list

        for words in s:
            if spaces == k: #when spaces is equal to number of words needed
                updatedString.pop() #removes last space that was appended
                break #break out of loop
            elif words == " ": #if a space is found
                spaces += 1 #increment space counter
                updatedString.append(words) #add space to list
            else:
                updatedString.append(words) #add letters to updated list
        
        updatedString = "".join(updatedString) #join letters together to form words in updated string

        return updatedString #return output
