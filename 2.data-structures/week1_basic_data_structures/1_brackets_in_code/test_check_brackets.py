import unittest
from check_brackets import find_mismatch

def unitTest(func, filename, debug):
    with (open("./tests/" + filename, "r") as inp, open("./tests/" + filename + ".a", "r") as out):
        inputValue, outputValue = inp.read(), out.read()
        result = func(inputValue)
        
        if debug:
            print(inputValue, outputValue, result)
        return outputValue.strip() == result

class TestCheckBrackets(unittest.TestCase):
    def test_all_inputs(self):
        debug = False
        for testNum in range(1, 55):
            self.assertTrue(unitTest(find_mismatch, str(testNum).zfill(2), debug))
            print("test" + str(testNum) + " passed!")


if __name__ == '__main__':
    unittest.main()
