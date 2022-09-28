import unittest
import sheep_talk_machine as sheepmach
import d_recognize as drec

class TestDRecognize(unittest.TestCase):
    def setUp(self):
        self.machine = sheepmach.SheepTalkMachine()
        self.valid_input = ["b","a","a","!"]
        self.invalid_input = ["b","a","!","!"]

    def test_returns_accept_for_valid_input(self):
        self.assertEqual("accept", drec.d_recognize(self.valid_input, self.machine))


class TestSheepTalkMachine(unittest.TestCase):
    def setUp(self):
        self.machine = sheepmach.SheepTalkMachine()

    def test_delta_returns_new_state_for_valid_transition(self):
        self.assertEqual(1, self.machine.delta(0, "b"))
        
if __name__ == '__main__':
    unittest.main()
    
