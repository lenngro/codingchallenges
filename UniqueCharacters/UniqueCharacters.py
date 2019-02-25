class UniqueCharacters:

	@staticmethod
	def isUnique(word):
		"""
		Test if a word consists only of unique characters.
		:param word:
		:return: True if the word consists of only unique characters, False if not
		"""

		uniqueLetters = {}

		for char in word:

			if char not in uniqueLetters:
				uniqueLetters[char] = 1
			else:
				return False

		return True


uc = UniqueCharacters()
print(uc.isUnique("word"))
