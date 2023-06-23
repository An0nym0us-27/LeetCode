class Solution {
public:
    vector<int> shuffle(vector<int>& nums, int n) {
        vector<int> shuffled; //new vector to store shuffled vals

        //shuffle vector and push back vals
        for(int i = 0; i < n; i++){
            int j = n;
            
            shuffled.push_back(nums[i]);
            shuffled.push_back(nums[i+j]);
        }
        return shuffled; //return shuffled vector
    }
};
