class Solution {
public:
    bool isMonotonic(vector<int>& nums) {
        int c = 0;
        int c1 = 0;
        for (int i = 0; i < nums.size() - 1; i++) {
            if (c > 0 && c1 > 0) {
                return false;
            }
            else if(nums[i]>nums[i+1]){
                c+=1;
            }
            else if(nums[i]<nums[i+1]){
                c1+=1;
            }
        }
        if (c > 0 && c1 > 0) {
            return false;
        }
        return true;
    }
};