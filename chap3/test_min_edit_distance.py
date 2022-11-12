import unittest
import min_edit_distance as edit_dist

class TestEditDistance(unittest.TestCase):
    def setUp(self):
        self.target = "execution"
        self.source = "intention"
        self.empty_string = ""

    def test_edit_distance_when_target_is_empty_string(self):
        self.assertEqual(
                edit_dist.get_distance("", self.source),
                len(self.source)
        )

    def test_edit_distance_when_source_is_empty_string(self):
        self.assertEqual(
                edit_dist.get_distance("", self.source),
                len(self.source)
        )

    def test_edit_distance_when_source_and_target_are_different(self):
        self.assertEqual(
                edit_dist.get_distance(self.target, self.source),
                8
        )

if __name__ == '__main__':
    unittest.main()
 
