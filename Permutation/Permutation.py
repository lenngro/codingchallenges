class Permutation:

    @staticmethod
    def isPermutation(str1, str2):
        """
        Check if one string is a permutation of another.
        :param str1: First string
        :param str2: Second string
        :return: Return True if one string is a permutation of the other, return False if not
        """

        if sorted(str1) == sorted(str2):

            return True

        return False

p = Permutation()
print(p.isPermutation("word", "wrod1"))
