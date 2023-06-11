class Solution {
public:
    int xorOperation(int n, int start) {
        int ans = 0; //xor result

        //array declaration
        int* nums = new int[n];
        for(int i = 0; i < n; i++){
            nums[i] = (start + 2 * i);
            ans ^= nums[i];
        }
        delete[] nums; //deallocate nums memory

        return ans; //return xor result
    }
};
