class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        #append the first given int to output list
        #xor given int to next int in encoded 
        #append to output list
        #repeat until encoded list is empy
      
        output = [first]
        decodeVar = first
        for i in encoded:
            decodeVar ^= i
            output.append(decodeVar)

        return output
