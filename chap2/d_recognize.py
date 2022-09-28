def d_recognize(tape, machine):
    # Implementation of pseudo-code example in Figure 2.12
    curr_cell = tape[0]
    current_state = machine._START

    print("curr_cell: ", curr_cell, " current_state: ", current_state)

    while True:
        if tape == []:
            if current_state in machine._F:
                return "accept"
            else:
                return "reject"
        elif machine.delta(current_state, curr_cell) == False:
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
