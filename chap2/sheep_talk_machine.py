class SheepTalkMachine:

    def __init__(self):
        print("New SheepTalkMachine Ready!")

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
    _STATE_TRANSITION_TABLE = { _START: {'b': 1, 'a': False, '!': False},
            1: { 'b': False, 'a': 2, '!': False },
            2: { 'b': False, 'a': 3, '!': False },
            3: { 'b': False, 'a': 3, '!': _F[0] },
            4: { 'b': False, 'a': False, '!': False },
            }

    # Operates over the state transition table
    def delta(self, q, s):
        if q in self._Q and s in self._S:
            return self._STATE_TRANSITION_TABLE[q][s]


