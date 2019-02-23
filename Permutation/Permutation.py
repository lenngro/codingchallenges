class Permutation:

    def isPermutation(self, str1, str2):

        if sorted(str1) == sorted(str2):

            return True

        return False

p = Permutation()
print(p.isPermutation("word", "wrod1"))
