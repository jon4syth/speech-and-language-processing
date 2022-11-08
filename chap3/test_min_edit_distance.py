import unittest
import min_edit_distance as edist

class TestEditDistance(unittest.TestCase):
    def setUp(self):
        self.target = "execution"
        self.source = "intention"

    def test_returns_a_number(self):
        self.assertEqual(edist.get_min_edit_distance(self.target, self.source), 5)


if __name__ == '__main__':
    unittest.main()
 
