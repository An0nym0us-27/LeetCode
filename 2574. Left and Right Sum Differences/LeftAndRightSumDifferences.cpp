class Solution {
public:
    vector<int> leftRightDifference(vector<int>& nums) {
        int l = nums.size();
        int updatedLeft = 0; //store current left sum
        int updatedRight = 0; //store current right sum
        
        vector<int> answer(l); //answer vector

        for(int i = 0; i < l; i++){ // finds right sums
           answer[i] = updatedRight;
           updatedRight += nums[i];
        }
        for(int i = l - 1; i >= 0; i--){ //finds left sum and subtracts absolute right from left sums simultaneously
            answer[i] = abs(answer[i] - updatedLeft);
            updatedLeft += nums[i];
        }
        return answer; //returns answer
    }
};
