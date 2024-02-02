class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        widths = [] #store x values
        gw = 0 #greatest width

        for i in range(len(points)): #store every x value in new list
            widths.append(points[i][0])
        
        widths.sort() #sort the list
        
        for i in range(len(widths) - 1): #subtract x values to find gw
            diff = widths[i + 1] - widths[i] #subtract next index from current
            gw = max(gw, diff) #compare diff to gw, keep whichever is greater

        return gw #output
