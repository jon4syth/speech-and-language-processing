import unittest
import sheep_talk_machine_v2 as sheepmach
import nd_recognize as ndrec

class TestDRecognize(unittest.TestCase):
    def setUp(self):
        self.machine = sheepmach.SheepTalkMachine()

    def test_returns_accept_for_valid_input(self):
        valid_input = ["b","a","a","!"]
        self.assertEqual("accept", ndrec.recognize(valid_input, self.machine))

    def test_rejects_invalid_input(self):
        invalid_input = ["b","a","!","!"]
        self.assertEqual("reject", ndrec.recognize(invalid_input, self.machine))

    def test_next_takes_search_state_off_of_agenda_and_returns_it(self):
        agenda = [(2,2), (3,2)]
        functionsfunctions
        self.assertEqual((2,2), ndrec.next(agenda))
        self.assertEqual([(3,2)], agenda)

    def test_can_generate_list_of_new_states(self):
        self.assertEqual(
            [2,3],
            ndrec.generate_new_states((2,2),
            self.machine)
        )

    def test_delta_returns_list_of_states_for_decision_point(self):
        self.assertEqual([2,3], self.machine.delta(2, "a"))

        
if __name__ == '__main__':
    unittest.main()
    
