class Solution {
public:
    vector<int> leftRightDifference(vector<int>& nums) {
        int l = nums.size();
        int updatedLeft = 0;
        int updatedRight = 0;
        
        vector<int> answer(l);

        for(int i = 0; i < l; i++){
           answer[i] = updatedRight;
           updatedRight += nums[i];
        }
        for(int i = l - 1; i >= 0; i--){
            answer[i] = abs(answer[i] - updatedLeft);
            updatedLeft += nums[i];
        }
        return answer;
    }
};
