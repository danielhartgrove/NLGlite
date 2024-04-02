import unittest


class stochasticsTest(unittest.TestCase):
    def test_generate_number_in_range(self):
        i = 1
        for j in range(1, 100):
            self.assertTrue(generate_number(i, j) <= j)
            self.assertTrue(generate_number(i, j) >= i)

    def test_generate_number_bad_return(self):
        i = 2
        j = 1
        self.assertTrue(generate_number(i, j) == -1)

    def test_generate_number_doesnt_allow_negatives(self):
        i = -1
        j = 2
        self.assertTrue(generate_number(i, j) == -1)

# TODO: test other method


if __name__ == '__main__':
    unittest.main()
