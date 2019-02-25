class POP:

    @staticmethod
    def isPermutationOfPalindrome(str1):
        """
        Test if the string can be represented as palindrome.
        :param str1:
        :return: True if there is a representation of the letters of the string that is a palindrome, False if not
        """

        letters = {}
        for char in str1:

            if char not in letters:
                letters[char] = 1
            else:
                letters[char] += 1

        nWrong = 0
        for value in letters.values():

            if value%2 != 0:
                nWrong += 1

            if nWrong > 1:
                return False

        return True

pop = POP()
print(pop.isPermutationOfPalindrome("aabbcc"))
