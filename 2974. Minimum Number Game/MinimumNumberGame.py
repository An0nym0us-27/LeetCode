class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        arr = [] #output array
        alice = 0 
        bob = 0
        while len(nums) > 0: #while list not empy
            alice = min(nums) #store minimum int in alice
            nums.remove(min(nums)) #remove min int
            bob = min(nums) #store next min int
            arr.append(bob)#append bob min int to output arr
            nums.remove(min(nums)) #remove bob min int
            arr.append(alice) #append alice min int to output arra
        return arr #return output


#O(N)
