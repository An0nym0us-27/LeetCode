class Solution {
public:
    vector<int> buildArray(vector<int>& nums) {
        vector<int> ans;
        int ns = nums.size();

        for(int i = 0; i < ns; i++){
            ans.push_back(nums[nums[i]]);
        }
        return ans;
    }
};
