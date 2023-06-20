class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        int n = nums.size(); //nums size
        int size = 2 * n; //var for scalability
        vector<int> ans(size); //vector declaration

        for(int i = 0; i < n; i++){ //fill indices 0-2
            ans[i] = nums[i];
        }
        for(int i = n; i < size; i++){ //fill indices 3-5
            ans[i] = nums[i-n];
        }

        return ans; //return concatenated vector
    }
};
