#this is not my code, I used to learn more about hash maps

    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        return sum( n+diff in nums and n+diff*2 in nums for n in nums )
#Whenever true add one to the counter, if n + difference is found and n + difference * 2 is found because j == diff + i and k == diff + diff + i
