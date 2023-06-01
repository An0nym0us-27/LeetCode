class Solution {
public:
    int subtractProductAndSum(int n) {
        //variable declaration
        long product = 1;
        int sum = 0;
        int ans;
        int element;

        vector<int> temp; //vector declaration

        //fill vector indivudally with each element
        while(n > 0){
            element = n % 10;
            temp.push_back(element);
            n /= 10;
        }
        
        //solve for the product and sum
        for(int i = 0; i < temp.size(); i++){
            product *= temp[i];
            sum += temp[i];
        }
        
        //subtract product and sum and return answer
        ans = product - sum;
        return ans;
    }
};
