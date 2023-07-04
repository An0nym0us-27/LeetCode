class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        accountSums = [] #store account sums
      
        for accountMoney in accounts: #find sum and store in list
            totalMoney = sum(accountMoney)
            accountSums.append(totalMoney)
        
        wealth = max(accountSums) #store max value

        return wealth #return highest value



