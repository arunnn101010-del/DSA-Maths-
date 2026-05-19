# Promblem - palindrome number
# Appraoch - maths + number manuplation
# Time and space complexity - 0(log n) & 0(1)
# Leetcode and diffculty level - 9 & easy
class Solution {
public:
    bool isPalindrome(int x) {
        if(x < 0) {
            return false;
        }
        int original = x;
        long long rev = 0;
        while(x > 0) {
            int digit = x % 10;
            rev = rev * 10 + digit;
            x = x/10;
        }
        return original == rev;
    }
};
