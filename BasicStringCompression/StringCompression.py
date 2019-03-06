class StringCompression:

    @staticmethod
    def compress(string):
        """
        A basic string compression. Replace multiple in-order occurrences of a letter
        by the letter and the sum of occurrences at that point:
        aaabbbb => a3b4
        acccc => ac4
        If the length of the compressed string is greater or equal to the original string,
        return the original.
        a => a
        aa => aa
        aaa => a3
        """

        compressed_string = ""
        counter = 1

        if len(string) == 1:
            return string

        for i in range(1, len(string)):
            if (string[i-1] == string[i]):
                counter += 1
            else:
                compressed_string += string[i-1]
                compressed_string += str(counter)
                counter = 1
        compressed_string += string[i]
        compressed_string += str(counter)

        if len(compressed_string) < len(string):
            return compressed_string
        else:
            return string

sc = StringCompression()
print(sc.compress("aaa"))
