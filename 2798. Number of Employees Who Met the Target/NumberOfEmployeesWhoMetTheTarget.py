class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        cntr = 0 #counter
        for i in hours: #if array value is greater than target hours, increment counter by 1
            if i >= target:
                cntr += 1
            else:
                pass #else do nothing
        return cntr #return counter
