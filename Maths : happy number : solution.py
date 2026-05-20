# Promblem - happy number
# Appraoch - binary search 
# Time and space complexity - 0(log n) & 0(log n)
# Leetcode and space complexity - 202 & easy 
class Solution {
public:
    bool isHappy(int n) {
        unordered_set<int> seen;

        while(n != 1 && seen.find(n) == seen.end()) {
            seen.insert(n);

            int sum = 0;

            while(n > 0) {
                int digit = n % 10;
                sum += digit * digit;
                n = n / 10;
            }
            n = sum;
        }
        return n == 1;
    }
};
