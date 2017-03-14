import unittest

def removeNegs(numList):
    """
    Function that takes a list of numbers and removes
    the negative numbers from the list
    """
    listLen = len(numList)
    for i in range(listLen):
        if numList[listLen-i-1] < 0:
            numList.pop(listLen-i-1)

    return numList

def sortList(numList):
    """
    Function takes a list of number and returns the list
    sorted from small to large
    """
    return sorted(numList)

def removeNegsAndSort(numList):
    """
    Function takes a list of numbers and returns a list
    of its non-negative values sorted from small to large
    """
    return sortList(removeNegs(numList))

def copyList(numList):
    """
    Function takes a list and returns a copy of it
    This function is used when you don't want to change
    the original list
    """
    copy = []

    for i in numList:
        copy.append(i)

    return copy

class TestRemoveNegs(unittest.TestCase):

    def setUp(self):
        """
        Runs before unitTests.
        Function sets up test list
        """
        self.newList = [5, -4, 2, -3, 1]

    def test_no_negs(self):
        """
        Function tests removeNegs Function
        """
        testList = copyList(self.newList)
        self.assertEqual(removeNegs(testList), [5, 2, 1])

    def test_sorted(self):
        """
        Function tests sortList Function
        """
        test = copyList(self.newList)
        self.assertEqual(sortList(test), [-4, -3, 1, 2, 5])

    def test_both(self):
        """
        Function tests sortList and removeNegs in tandem
        """
        test = copyList(self.newList)
        self.assertEqual(removeNegsAndSort(test), [1, 2, 5])


if __name__ == '__main__':
    unittest.main()
