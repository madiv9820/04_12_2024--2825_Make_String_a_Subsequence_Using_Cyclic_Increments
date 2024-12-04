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