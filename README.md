# Make String a Subsequence Using Cyclic Increments (All Approaches)

- ## Approach 1:- Two Pointers using Recursion

    - ### Intuition
        The problem requires checking if we can form the string `str2` as a subsequence of `str1` by allowing each character in `str1` to either:
        1. Match the current character in `str2`.
        2. Be incremented (in the alphabet) to match the current character in `str2`.

        The idea is to use recursion to try to match characters one by one from `str2` with characters from `str1`. For each character in `str1`, we either:
        - Move to the next character in both strings if they match.
        - Skip the character in `str1` and try again if they don't match, while checking if an incremented character in `str1` matches the current character in `str2`.

        The problem can be solved efficiently with recursion and backtracking by attempting all possible ways to form `str2` from `str1`.

    - ### Approach
        1. **Base Case 1**: If we have matched all characters of `str2` (`index2 == str2_length`), return `true` since we have successfully formed `str2`.
        2. **Base Case 2**: If we reach the end of `str1` (`index1 == str1_length`) without matching all characters of `str2`, return `false` because it's impossible to form `str2`.
        3. For each character in `str1`, check if it matches the current character in `str2`. If so, recurse with both indices incremented.
        4. If the characters do not match, check if the current character in `str1` can be incremented to match the current character in `str2`. If it can, recurse with both indices incremented.
        5. If neither condition is met, move to the next character in `str1` (increment `index1`) and try again with the same `index2`.

        The function `check(index1, index2)` is called recursively, which checks if `str2[index2:]` can be matched as a subsequence of `str1[index1:]`.

    - ### Code Implementation
        - **Python Solution**
            ```python3 []
            class Solution:
                def canMakeSubsequence(self, str1: str, str2: str) -> bool:
                    # Get the lengths of the two input strings
                    str1_Length, str2_Length = len(str1), len(str2)
                    
                    # Recursive helper function to check if str2 can be formed as a subsequence of str1
                    def check(index1: int, index2: int) -> bool:
                        # If we've matched all characters in str2, return True
                        if index2 == str2_Length: return True
                        
                        # If we've reached the end of str1 without matching all characters of str2, return False
                        if index1 == str1_Length: return False

                        # If the characters at the current indices in str1 and str2 match, move to the next character in both strings
                        if str1[index1] == str2[index2]: return check(index1+1, index2+1)
                        
                        # Get the current character in str1
                        currentCharacter = str1[index1]
                        # Calculate the next character in the alphabet, wrapping from 'z' to 'a'
                        changedCharacter = 'a' if currentCharacter == 'z' else chr(ord(currentCharacter)+1)

                        # If the next character in str1 matches the current character in str2, move to the next character in both strings
                        if changedCharacter == str2[index2]: return check(index1+1, index2+1)

                        # Otherwise, just move to the next character in str1 and try again
                        return check(index1+1, index2)
                    
                    # Start the recursive checking from the beginning of both strings
                    return check(0, 0)
            ```
        
        - **C++ Solution**
            ```cpp []
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
            ```

    - ### Time Complexity
        The time complexity of this approach is **O(str1_length * str2_length)**, where `str1_length` is the length of `str1` and `str2_length` is the length of `str2`. This is because:
        - We perform a recursive check for each combination of indices `index1` (for `str1`) and `index2` (for `str2`).
        - At each recursive call, we either:
            - Move to the next character in `str1` and try to match the next character in `str2`, or
            - Skip a character in `str1` and keep the current character in `str2`.

        Since in the worst case we explore every character in both strings, the time complexity is proportional to the product of their lengths.

    - ### Space Complexity
        The space complexity of this solution is **O(str1_length + str2_length)** due to the following reasons:
        1. **Recursive Call Stack**: The recursion depth can go as deep as the lengths of both strings, i.e., `O(str1_length + str2_length)`, since in the worst case we may need to traverse both strings entirely.
        2. **Additional Space**: The function only uses a fixed amount of extra space for storing variables (e.g., `currentCharacter`, `changedCharacter`), which is constant (`O(1)`).

        Thus, the space complexity is dominated by the recursive call stack, leading to **O(str1_length + str2_length)**.

- ## Approach 2:- Two Pointers using Iteration

    - ### Intuition:
        The problem is to check whether we can transform `str1` into `str2` by performing a sequence of operations. Specifically, for each character in `str1`, we can either:
        1. Match it directly with the corresponding character in `str2`.
        2. Increment the character in `str1` by 1 (i.e., 'a' becomes 'b', 'b' becomes 'c', ..., 'z' wraps back to 'a') and match the incremented character with the corresponding character in `str2`.

        To solve this problem, we need to check whether we can traverse through `str1` and match all characters of `str2` by either direct matching or by incrementing characters.

    - ### Approach:
        1. **Two Pointers**: Use two pointers (`index1` and `index2`) to iterate through `str1` and `str2` respectively.
            - `index1` will traverse through each character of `str1`.
            - `index2` will track which character in `str2` we are currently trying to match.
        2. **Character Matching**:
            - If `str1[index1]` matches `str2[index2]`, increment `index2` to move to the next character in `str2`.
            - If `str1[index1]` doesn't match `str2[index2]`, increment the character in `str1` by one (i.e., move from 'a' to 'b', 'b' to 'c', etc.) and check if it matches `str2[index2]`. If it matches, increment `index2`.
        3. **Termination Condition**:
            - If `index2` reaches the end of `str2`, it means we've successfully matched all characters of `str2` in `str1`, so return `true`.
            - If we finish iterating through `str1` without fully matching `str2`, return `false`.
        4. **Final Check**: After the loop ends, if we have matched all characters of `str2` (i.e., `index2 == str2_length`), return `true`. Otherwise, return `false`.

    - ### Code Implementation
        - **Python Solution**
            ```python3 []
            class Solution:
                def canMakeSubsequence(self, str1: str, str2: str) -> bool:
                    # Initialize index2 to track position in str2
                    # Also, store lengths of str1 and str2
                    index2, str1_Length, str2_Length = 0, len(str1), len(str2)

                    # Iterate over str1 to check for matching subsequence
                    for index1 in range(str1_Length):
                        # If we have matched all characters of str2, return True
                        if index2 == str2_Length: return True

                        # If characters in str1 and str2 match, move to the next character in str2
                        if str1[index1] == str2[index2]: index2 += 1
                        else:
                            # Calculate the next character in str1 (increment it)
                            currentCharacter = str1[index1]
                            # If the character is 'z', reset to 'a', otherwise move to the next character
                            changedCharacter = 'a' if currentCharacter == 'z' else chr(ord(currentCharacter) + 1)

                            # If the incremented character matches str2[index2], move to the next character in str2
                            if changedCharacter == str2[index2]: index2 += 1
                    
                    # If we have matched all characters of str2 by the end of str1, return True
                    if index2 == str2_Length: return True
                    
                    # If we finish iterating through str1 but haven't matched all of str2, return False
                    return False
                    
                    '''
                    # Alternative solution using a while loop (commented out for reference):
                    # Initialize pointers for both strings
                    index1, index2 = 0, 0
                    str1_Length, str2_Length = len(str1), len(str2)

                    # Iterate over str1 to check for matching subsequence
                    while index1 < str1_Length:
                        # If we've matched all characters in str2, return True
                        if index2 == str2_Length: return True
                        
                        # If the characters in str1 and str2 match, move to the next character in str2
                        if str1[index1] == str2[index2]: index2 += 1
                        else:
                            # Calculate the next character in str1 (increment it)
                            currentCharacter = str1[index1]
                            # If the character is 'z', reset to 'a', otherwise move to the next character
                            changedCharacter = 'a' if currentCharacter == 'z' else chr(ord(currentCharacter) + 1)

                            # If the incremented character matches str2[index2], move to the next character in str2
                            if changedCharacter == str2[index2]: index2 += 1
                        
                        # Move to the next character in str1
                        index1 += 1

                    # If we've matched all characters of str2 by the end of str1, return True
                    if index2 == str2_Length: return True

                    # If we finish iterating through str1 but haven't matched all of str2, return False
                    return False
                    '''
            ```
        
        - **C++ Solution**
            ```cpp []
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
            ```

    - ### Time Complexity:
        - **O(str1_length)**: We only traverse through `str1` once. Each character comparison or increment operation takes constant time, and `index1` is incremented with each iteration.
        - In the worst case, we will traverse all characters of `str1` and potentially check multiple increments, but the total number of steps depends directly on the length of `str1`, so the overall time complexity is **O(str1_length)**.

    - ### Space Complexity:
        - **O(1)**: We are using only a few integer variables (`index1`, `index2`, `str1_Length`, `str2_Length`), so the space complexity is constant. No additional data structures are used, and the space does not depend on the input size.