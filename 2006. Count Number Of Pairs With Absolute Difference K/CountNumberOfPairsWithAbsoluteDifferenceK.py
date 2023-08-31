class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        dict = {} #dictionary
        pairs = 0 #keep track of pairs

        for num in nums: #loop for creating dictionary
            if num in dict:
                dict[num] += 1 #increase frequency if exists in dictionary
            else:
                dict[num] = 1 #add to dictionary and initialize dictionary frequency to 1

        for num in dict:
            if num - k in dict: #if the difference is found in dictionary
                pairs += dict[num - k] * dict[num] #multiply the occurence by the frequency of it in the dictionary

        return pairs #return pairs
