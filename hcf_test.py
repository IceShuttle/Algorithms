import unittest

import hcf


class hcftest(unittest.TestCase):
    def test_values(self):
        self.assertEqual(hcf.list_hcf([10, 15, 20]), 5)
        self.assertEqual(hcf.list_hcf([10, 20, 40]), 10)

    def test_datatype(self):
        self.assertIsInstance(hcf.list_hcf([10, 15, 20]), int)


if __name__ == "__main__":
    unittest.main()
