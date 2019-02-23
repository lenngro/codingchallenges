class OneOrZeroEdits:

    def editsAway(self, str1, str2):

        #str1 = sorted(str1)
        #str2 = sorted(str2)

        if str1 == str2:

            return 0

        edits = 0
        for i in range(len(str1)):

            if str1[i] != str2[i]:

                edits += 1

        if edits == 1:

            return 1
ozoe = OneOrZeroEdits()
print(ozoe.editsAway("word", "wrod"))
