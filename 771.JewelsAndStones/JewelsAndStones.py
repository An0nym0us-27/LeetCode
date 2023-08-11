class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        counter = 0

        for i in range(0, len(jewels)): #traverse jewels list
            current = jewels[i]
            for i in range(0, len(stones)): #traverse Stones list
                if current == stones[i]:
                    counter += 1  #increment if index values match
                    
        return counter #return counter
