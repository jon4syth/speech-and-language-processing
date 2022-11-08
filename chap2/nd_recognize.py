class NDRecognize:
    def __init__(self, tape):
        self.tape = tape

def recognize(tape, machine):
    # An implementation of the pseudo-code example in Figure 2.19 (p. 35).
    #
    # This implementation uses the symbol on the tape as the second item in the
    # search state tuple rather then the index (as in Fig 2.19). I made this
    # change after running into the problem of not having the tape available in
    # the `generate_new_states` function to pull the symbol from based on the
    # index, because the example only specifies the node and index as the
    # members of the search state tuple (the only parameter to that function).
    agenda = [(machine._START, 0)]
    current_search_state = next(agenda)

    print("current_search_state: ", current_search_state)

    while True:
        if tape == []:
            if current_state in machine._F:
                return "accept"
            else:
                return "reject"
        elif machine.delta(current_search_state) == False:
            return "reject"
        else:
            print("not at the end yet")
            current_state = machine.delta(current_state, curr_cell)
            tape.pop(0)

            try:
                curr_cell = tape[0]
            except IndexError:
                print("End of tape")

            print("curr_cell: ", curr_cell, " current_state: ", current_state)


# returns a list of search states
def generate_new_states(current_search_state, machine):
    current_node = current_search_state[0]
    index = current_search_state[1]

    return machine.delta(current_node, tape[index])

# retrieves the next agenda item (search state) from the
# begining of the list, altering agenda by removing the same
def next(agenda):
    return agenda.pop(0)
