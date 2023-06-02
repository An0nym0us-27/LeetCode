class Solution {
public:
    int sumOfMultiples(int n) {
        //vector & var declaration
        vector<int> range(n - 1);
        vector<int> divnums;
        int sum = 0;
    
        iota(range.begin(), range.end(), 2); //fill vector with range

        //find divisible numbers
        for(int i = 1; i < range.size(); i++){
            if((range[i] % 3 == 0) || (range[i] % 5 == 0) || (range[i] % 7 == 0)){
              divnums.push_back(range[i]);
            }
        }
        //find sum of divisble numbers
        for(int i = 0; i < divnums.size(); i++){
            sum += divnums[i];
        }

        return sum;
    }
};
