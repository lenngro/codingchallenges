class OneOrZeroEdits:

    @staticmethod
    def editsAway(str1, str2):
        """
        Check if one string can be edited to another string in either 0 or 1 steps.
        :param str1: First string
        :param str2: Second string
        :return: 1 if strings can be made equal in 0 or 1 steps, 0 if not
        """

        if str1 == str2:

            return 1

        edits = 0

        if len(str1) > len(str2):

            for i in range(len(str2)):

                if str1[i] != str2[i]:
                    edits += 1

            edits += len(str1[len(str2):len(str1)])

        elif len(str1) < len(str2):

            for i in range(len(str1)):

                if str1[i] != str2[i]:
                    edits += 1

            edits += len(str2[len(str1):len(str2)])

        else:

            for i in range(len(str1)):

                if str1[i] != str2[i]:
                    edits += 1

        if edits < 2:

            return 1
        else:
            return 0

ozoe = OneOrZeroEdits()
print(ozoe.editsAway("word", "wordss"))
