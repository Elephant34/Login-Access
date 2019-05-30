'''
Converts a text writen number into an integer
'''


class Illegal_Word(Exception):  # pylint: disable=invalid-name
    '''
    Custom exception for invalid words
    '''

    def __init__(self, message=""):  # pylint: disable=useless-super-delegation

        # Calls the Exceptions initialization method
        super().__init__(message)


def text2int(textnum, numwords=None):
    '''
    Converts a writen number to integer

    Credit to stackoverflow user: https://stackoverflow.com/users/44743/recursive
    '''
    if not numwords:
        numwords = {}
        units = [
            "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
            "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
            "sixteen", "seventeen", "eighteen", "nineteen",
        ]

        tens = ["", "", "twenty", "thirty", "forty",
                "fifty", "sixty", "seventy", "eighty", "ninety"]

        scales = ["hundred", "thousand", "million", "billion", "trillion"]

        numwords["and"] = (1, 0)
        for idx, word in enumerate(units):
            numwords[word] = (1, idx)
        for idx, word in enumerate(tens):
            numwords[word] = (1, idx * 10)
        for idx, word in enumerate(scales):
            numwords[word] = (10 ** (idx * 3 or 2), 0)

    current = result = 0
    for word in textnum.split():
        if word not in numwords:
            raise Illegal_Word

        scale, increment = numwords[word]
        current = current * scale + increment
        if scale > 100:
            result += current
            current = 0

    return result + current


# try:
#    print(text2int(str(input(""))))
# except Illegal_Word:
#    pass
