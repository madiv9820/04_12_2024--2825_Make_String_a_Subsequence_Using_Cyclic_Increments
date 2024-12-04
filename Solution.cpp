#include <iostream>
#include <string>
#include <functional>
using namespace std;

class Solution {
public:
    bool canMakeSubsequence(string str1, string str2) {
        // Get the lengths of the two input strings
        int str1_Length = str1.length(), str2_Length = str2.length();

        // Recursive lambda function to check if str2 can be formed as a subsequence of str1
        function<bool(int, int)> check = [&](int index1, int index2) -> bool {
            // If we've matched all characters in str2, return true (we have successfully formed the subsequence)
            if(index2 == str2_Length) return true;
            
            // If we've reached the end of str1 without matching all characters of str2, return false
            if(index1 == str1_Length) return false;

            // If the characters at the current indices in str1 and str2 match, move to the next character in both strings
            if(str1[index1] == str2[index2]) return check(index1+1, index2+1);
            
            // Get the current character in str1
            char currentCharacter = str1[index1];
            // Calculate the next character in the alphabet (wrapping from 'z' to 'a')
            char changedCharacter = (currentCharacter == 'z') ? 'a': currentCharacter + 1;

            // If the next character in str1 matches the current character in str2, move to the next character in both strings
            if(changedCharacter == str2[index2]) return check(index1+1, index2+1);

            // Otherwise, just move to the next character in str1 and try again with the same character in str2
            return check(index1+1, index2);
        };

        // Start the recursive checking from the beginning of both strings
        return check(0, 0);
    }
};

int main() {
    string str1 = "zc", str2 = "ad"; Solution sol;
    cout << (sol.canMakeSubsequence(str1, str2) ? "true": "false") << endl;
}