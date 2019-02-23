class UniqueCharacters:
	def isUnique(self, word):

		uniqueLetters = {}

		for char in word:

			if char not in uniqueLetters:
				uniqueLetters[char] = 1
			else:
				return False
		return True


uc = UniqueCharacters()
print(uc.isUnique("woord"))
