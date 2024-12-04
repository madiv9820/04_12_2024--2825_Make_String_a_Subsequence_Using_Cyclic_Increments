#include <iostream>
#include <string>
using namespace std;

class Solution {
public:
    bool canMakeSubsequence(string str1, string str2) {
        // Initialize pointers to track the current positions in str1 and str2
        int index1 = 0, index2 = 0;
        // Get the lengths of both strings for loop conditions
        int str1_Length = str1.length(), str2_Length = str2.length();

        // Iterate through str1 to check if we can form str2 as a subsequence
        for (; index1 < str1_Length; ++index1) {
            // If we've matched all characters in str2, return true
            if (index2 == str2_Length) return true;

            // If the characters at the current positions in str1 and str2 match, move to the next character in str2
            if (str1[index1] == str2[index2]) ++index2;
            else {
                // If characters don't match, calculate the next character in str1 (increment it)
                char currentCharacter = str1[index1];
                char changedCharacter = currentCharacter + 1; // Increment the character in str1

                // If the incremented character in str1 matches the current character in str2, move to the next character in str2
                if (changedCharacter == str2[index2]) ++index2;
            }
        }

        // After finishing the loop, check if all characters of str2 have been matched
        if (index2 == str2_Length) return true;

        // If we haven't matched all characters of str2 by the end of str1, return false
        return false;

        /*
        // Alternative solution using a while loop (commented out for reference):
        // Initialize pointers to track positions in both strings
        int index1 = 0, index2 = 0;
        // Get the lengths of both strings for loop conditions
        int str1_Length = str1.length(), str2_Length = str2.length();

        // Iterate through str1 to check for matching characters in str2
        while (index1 < str1_Length) {
            // If we've matched all characters of str2, return true
            if (index2 == str2_Length) return true;

            // If the characters in str1 and str2 match, move to the next character in str2
            if (str1[index1] == str2[index2]) {
                ++index2;
            } else {
                // If characters don't match, calculate the next character in str1
                char currentCharacter = str1[index1];
                // If the character is 'z', reset to 'a', otherwise move to the next character
                char changedCharacter = (currentCharacter == 'z') ? 'a' : currentCharacter + 1;  // Increment the current character

                // If the incremented character in str1 matches the current character in str2, move to the next character in str2
                if (changedCharacter == str2[index2]) {
                    ++index2;
                }
            }

            // Move to the next character in str1
            ++index1;
        }

        // After finishing iterating through str1, check if all characters of str2 have been matched
        if (index2 == str2_Length) return true;

        // If not all characters of str2 were matched, return false
        return false;
        */
    }
};

int main()  {
    Solution sol;
    cout << (sol.canMakeSubsequence("abc", "ad") ? "true":"false") << endl;
}