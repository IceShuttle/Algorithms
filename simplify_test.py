import unittest


from simplify import simplify


class simplifytest(unittest.TestCase):
    def test_datatype(self):
        self.assertIsInstance(simplify([4, 5]), list)

    def test_size(self):
        self.assertEqual(len(simplify([4, 5])), 2)

    def test_simplification(self):
        self.assertEqual(simplify([10, 15]), [2, 3])
        self.assertEqual(simplify([30, 15]), [2, 1])

    def test_num_zero_case(self):
        self.assertEqual(simplify([0, 30]), [0, 1])


if __name__ == "__main__":
    unittest.main()
