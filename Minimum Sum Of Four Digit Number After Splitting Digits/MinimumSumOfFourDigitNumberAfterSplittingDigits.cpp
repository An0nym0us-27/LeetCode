class Solution {
public:
    int minimumSum(int num) {
    //variable declaration
    int new1;
    int new2;
    string strTemp = to_string(num);

    //sort num
    sort(strTemp.begin(), strTemp.end());
    num = stoi(strTemp);

    //extract indexes
    new1 = (num / 1000) * 10 + ((num / 10) % 10);
    new2 = ((num / 100) % 10) * 10 + (num % 10);

    return new1 + new2; //return minimum sum
    }
};
