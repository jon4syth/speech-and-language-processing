# This version of the sheep talk machine includes the epsilon transition
# which is a state transition without advancing the tape index
class SheepTalkMachine:

    def __init__(self):
        print("New SheepTalkMachine V2 Ready!")

    #########
    # Five elements of a Finite State Machine (FSA)
    ############

    # Q - a set of states
    _Q = (0, 1, 2, 3, 4)
    # Sigma - a set of input symbols (letters in this case)
    _S = ("b", "a", "!")
    # A start State
    _START = 0
    # F- a set of final or "accepting" states which are a subset of Q
    _F = _Q[-1:]
    # A state transition table and/or function that returns a valid state for
    # a valid state/symbol pair
    # This version of the state transition table includes the key False
    # on each row to represent an epsilon-transition although it does
    # not return a valid state in this case (i.e. there are no epsilon-
    # transitions for this particular machine)
    _STATE_TRANSITION_TABLE = { 
      _START: {'b': 1, 'a': False, '!': False, False: False},
           1: { 'b': False, 'a': 2, '!': False, False: False },
           2: { 'b': False, 'a': [2,3], '!': False, False: False },
           3: { 'b': False, 'a': 3, '!': _F[0], False: False },
           4: { 'b': False, 'a': False, '!': False, False: False },
        }

    # Operates over the state transition table
    # accepts a search state tuple
    def delta(self, q, s):
        if q in self._Q and s in self._S:
            return self._STATE_TRANSITION_TABLE[q][s]


    def delta(self, q, s=False):
        if q in self._Q:
          return self._STATE_TRANSITION_TABLE[q][s]
