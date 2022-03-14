# Python 3 program to find first and last occurrence of an elements in given sorted array

class NumberSeries:
    pass

    def __init__(self, result):
        if result != None:
            self.result = result
        else:
            self.result = (-1, -1)

    # Function for finding first and last occurrence of an elements
    def findFirstAndLast(self, array, numberSearched):
        first = -1
        last = -1
        for i in range(0, len(array)):
            if (numberSearched != array[i]):
                continue
            if (first == -1):
                first = i
            last = i

        if (first != -1):
            return (first, last)
        else:
            return (-1, -1)
