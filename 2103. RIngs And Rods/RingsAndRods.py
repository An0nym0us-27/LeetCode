class Solution:
    def countPoints(self, rings: str) -> int:
        ans = 0 #tracks number of rods that have all three colors
        #for i in range(10) this was the original line of code
        for i in range(len(rings) - 1): #loop through the length of rings, this is the line of code I changed it to
            i = str(i) #convert i from an int to a string val for the line below
            if 'R'+i in rings and 'G'+i in rings and 'B'+i in rings: #search rod i for all three ring colors
                ans += 1 #incremement counter if rod i has all three color rings
        return ans #return number of rods with all three colors

  #This is not my code. This was a solution that I found that I liked. There was one line of code that I did change however because the previous line of code used only made this code usuable with a specific number of letters in the string. I left the original line but commented it out and implemented the new one. The line I modified change this from having a computational time complexity of O(1) to O(n).
  
