from Solution import Solution
import unittest
from timeout_decorator import timeout

class UnitTest(unittest.TestCase):
    def setUp(self):
        self.__testCases = {1: ('abc','ad',True), 2: ('zc','ad',True), 3: ('ab','d',False)}
        self.__obj = Solution()
        return super().setUp()
    
    @timeout(0.5)
    def test_Case_1(self):
        str1, str2, output = self.__testCases[1]
        result = self.__obj.canMakeSubsequence(str1 = str1, str2 = str2)
        self.assertIsInstance(result, bool)
        self.assertEqual(result, output)

    @timeout(0.5)
    def test_Case_2(self):
        str1, str2, output = self.__testCases[2]
        result = self.__obj.canMakeSubsequence(str1 = str1, str2 = str2)
        self.assertIsInstance(result, bool)
        self.assertEqual(result, output)

    @timeout(0.5)
    def test_Case_3(self):
        str1, str2, output = self.__testCases[3]
        result = self.__obj.canMakeSubsequence(str1 = str1, str2 = str2)
        self.assertIsInstance(result, bool)
        self.assertEqual(result, output)

if __name__ == '__main__': unittest.main()