class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort() #sort the list and place first two numbers in c & d respectively, place last two numbers in a & b respectively
        c = nums[0]
        d = nums[1]
        a = nums[-2]
        b = nums[-1]
        sum = (a*b) - (c*d) # multiply and subtract
        return sum #return sum
