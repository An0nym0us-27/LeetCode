class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        binaryList = [] #Store values that have k set bits
        for i in range(len(nums)): #loop through nums
            if bin(i).count("1") == k: #if the binary indice has set bits equal to k, append to new list
                binaryList.append(nums[i])
            else:
                pass #otherwise just continue
        return sum(binaryList) #returnt the sum of values
