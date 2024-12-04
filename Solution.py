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