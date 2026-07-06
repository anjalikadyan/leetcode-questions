#include <map>
class Solution {
public:
    int romanToInt(string s) {
        map<char, int> age;
        age['I'] = 1;
        age['V'] = 5;
        age['X'] = 10;
        age['L'] = 50;
        age['C'] = 100;
        age['D'] = 500;
        age['M'] = 1000;
        int sum = 0;
        char pre = s[0];
        for (char a : s) {
            if (age[pre] < age[a]) {
                sum += age[a];
                int d = 2 * age[pre];
                sum -= d;

            } else if (age[pre] >= age[a]) {
                sum += age[a];
            }
            pre = a;
        }
        return sum;
    }
};