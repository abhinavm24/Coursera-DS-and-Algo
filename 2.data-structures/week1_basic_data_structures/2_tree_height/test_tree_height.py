import unittest
from tree_height import compute_height as compute_height_raw
from tree_height_solution import compute_height as compute_height_improved


def unitTest(func, filename, debug):
    with (open("./tests/" + filename, "r") as inp, open("./tests/" + filename + ".a", "r") as out):
        n, parent, outputValue = int(
            inp.readline()), list(map(int, inp.readline().split())), out.read()
        result = func(n, parent)

        if debug:
            print(n, parent, outputValue, result)
        return int(outputValue.strip()) == result


class TestBruteBracketsRaw(unittest.TestCase):
    def test_all_inputs(self):
        debug = False
        for testNum in range(1, 17):
            self.assertTrue(
                unitTest(compute_height_raw, str(testNum).zfill(2), debug))
            print("test: " + str(testNum) + " passed!")


class TestBruteBracketsSolution(unittest.TestCase):
    def test_all_inputs(self):
        debug = False
        for testNum in range(1, 25):
            self.assertTrue(unitTest(compute_height_improved,
                            str(testNum).zfill(2), debug))
            print("test: " + str(testNum) + " passed!")


if __name__ == '__main__':
    unittest.main()
