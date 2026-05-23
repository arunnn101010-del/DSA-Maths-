# Promblem - find missing positive 
# Appraoch - index placement + cyclic sort 
# Time and space complexity - 0(n) & 0(1)
# Leetcode and diffculty level - 41 & hard
class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        int n = nums.size();

        for(int i=0; i<n; i++) {
            while(nums[i] > 0 && nums[i] <= n && nums[nums[i]-1] != nums[i]) {
                swap(nums[i], nums[nums[i]-1]);
            }
        }
        
        for(int i=0; i<n; i++) {
            if(nums[i] != i+1) {
                return i+1;
            }
        }
        return n+1;
    }
};
