# Promblem - sqrt(x)
# Approach - binary search + maths
# Time and space complexity - 0(log n) & 0(1)
# Leetcode and diffculty level - 69 & easy 
#class Solution {
public:
    int mySqrt(int x) {
        int low = 1;
        int high = x;
        int ans = 0;

        while(low <= high) {
            long long mid = low + (high - low) / 2;
            long long square = mid * mid;
            
            if(square == x) {
                return mid;
            }
            else if(square < x) {
                ans = mid;
                low = mid + 1;
            }
            else {
                high = mid - 1;
            }
        }
        return ans;
    }
};
