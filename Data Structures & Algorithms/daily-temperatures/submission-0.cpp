class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        int n = temperatures.size();
        std::stack<int> mono_s;
        std::vector<int> result(n);
        for (int i = n - 1; i >= 0; --i) {
            while (
                !mono_s.empty() 
                && temperatures[i] >= temperatures[mono_s.top()]
            ) {
                mono_s.pop();
            }
            result[i] = mono_s.empty() ? 0 : mono_s.top() - i;
            mono_s.push(i);
        }
        return result;
    }
};
