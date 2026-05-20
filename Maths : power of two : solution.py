# Promblem - power of two 
# Appraoch - bit manuplation 
# Time and space complexity - 0(1) & 0(1)
# Leetcode and diffculty level - 231 & easy 
class Solution {
public:
    bool isPowerOfTwo(int n) {
        if(x <= 0) {
            return false;
        }
        return (n & (n - 1)) == 0;
    }
};
