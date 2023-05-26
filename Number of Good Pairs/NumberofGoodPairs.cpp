class Solution {
public:
    int numIdenticalPairs(vector<int>& nums) {
        //variable declaration
        int pairs = 0;
        int v = nums.size();

        //for loop to traverse nums vector
        for(int i = 0; i < v - 1; i++){
            for(int j = i + 1; j < v; j++){
                if(nums[i] == nums[j]){
                    pairs++;
                }
            }
        }
        return pairs; //return number of pairs
    }
};
