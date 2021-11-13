import unittest
from tree_height import computeHeightOfTree

def unitTest(filename, debug):
    with (open("./tests/" + filename, "r") as inp, open("./tests/" + filename + ".a", "r") as out):
        n, parent, outputValue = inp.readline(), inp.readline(), out.read()
        result = computeHeightOfTree(n, parent)
        
        if debug:
            print(n, parent, outputValue, result)
        return int(outputValue.strip()) == result

class TestCheckBrackets(unittest.TestCase):
    def test_all_inputs(self):
        debug = False
        for testNum in range(1, 55):
            self.assertTrue(unitTest(str(testNum).zfill(2), debug))
            print("test" + str(testNum) + " passed!")


if __name__ == '__main__':
    unittest.main()
