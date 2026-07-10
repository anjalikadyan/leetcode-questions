class Solution {
public:
    vector<int> xorQueries(vector<int>& arr, vector<vector<int>>& queries) {
        vector<int> s(arr.size() + 1, 0);
        for (int i = 0; i < arr.size(); i++) {
            s[i + 1] = s[i] ^ arr[i];
        }
        vector<int> ans;
        ans.reserve(queries.size());
        for (auto& q : queries) {
            int a = q[0], b = q[1];
            ans.push_back(s[b + 1]^s[a]);
        }
        return ans;
    }
};