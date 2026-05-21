# Promblem - reverse integer 
# Time and space complexity - 0(log n) & 0(1)
# Leetcode and diffculty level - 7 & medium
class Solution {
public:
    int reverse(int x) {

        int ans = 0;

        while(x != 0) {

            int digit = x % 10;

            if(ans > INT_MAX / 10 || ans < INT_MIN / 10) {
                return 0;
            }
            ans = ans * 10 + digit;
            x = x / 10;
        }
        return ans;
    }
};
