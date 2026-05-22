# Promblem - factorial trailing zeroes 
# Appraoch - maths 
# Time and space complexity - 0(log n) & 0(1)
# Leetcode and diffculty level - 172 & medium 
class Solution {
public:
    int trailingZeroes(int n) {
        int ans = 0;

        while(n > 0) {
            n = n/5;
            ans += n;
        }
        return ans;
    }
};
