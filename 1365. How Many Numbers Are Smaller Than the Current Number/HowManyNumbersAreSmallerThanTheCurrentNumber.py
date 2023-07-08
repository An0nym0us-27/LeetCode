class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        output = [] #output list
        for i in nums:
            counter = 0
            for j in nums: #compare current index to the rest of the list
                if(i > j and i != j):
                    counter += 1 # increment if it satisfies the condition
            output.append(counter) #append counter to new list
        return output #return output list
