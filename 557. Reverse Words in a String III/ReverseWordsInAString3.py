class Solution:
    def reverseWords(self, s: str) -> str:
        rs = "" #output string
        temp = "" #temp string
        rsl = [] #temp list
        for i in s[::-1]: #place reversed words in new string
            rs += i
        
        rs += " " #add a space to detect stopping point
        for i in rs:
            if i == " ": #if a space is detected it means a full word has been found, append word to list and clear temp
                rsl.append(temp)
                rsl.append(" ")
                temp = ""
            else:
                temp += i #else continue adding letters to string until full word is created

        rs = "" #clear output string
        rsl.pop() #remove extra space that isn't needed for output
        for i in rsl[::-1]: #return the reverse order of the list and append it to output string
            rs += i

        return rs #return output
