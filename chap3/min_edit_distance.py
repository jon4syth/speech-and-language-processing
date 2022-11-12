def get_min_edit_distance(target, source):
    n = len(target)
    m = len(source)

    return n - m

# TODO: make a pseudo-overloadable distance function
# that can calculate distance from an empty string
# to a non-empty target string or vice versa
def get_distance(target="", source=""):
    if target == "" and source == "":
        return "Both args are empty strings!"

    cost = 0

    # cost of moving from non-zero length string to empty string
    if target == "":

        for char in source:
            cost = cost + deletion_cost(char)

        return cost

    # cost of moving from empty string to non-zero length string

# Cost of insertion--we could add a multiplier for certain letters
def insertion_cost(char):
    return cost_table[char]

# Cost of deletion--we could add a multiplier for certain letters
def deletion_cost(char):
    return cost_table[char]


## Cost Table for insertions and deletions
cost_table = ({
   'A': 1, 'a': 1,
   'B': 1, 'b': 1,
   'C': 1, 'c': 1,
   'D': 1, 'd': 1,
   'E': 1, 'e': 1,
   'F': 1, 'f': 1,
   'G': 1, 'g': 1,
   'H': 1, 'h': 1,
   'I': 1, 'i': 1,
   'J': 1, 'j': 1,
   'K': 1, 'k': 1,
   'L': 1, 'l': 1,
   'M': 1, 'm': 1,
   'N': 1, 'n': 1,
   'O': 1, 'o': 1,
   'P': 1, 'p': 1,
   'Q': 1, 'q': 1,
   'R': 1, 'r': 1,
   'S': 1, 's': 1,
   'T': 1, 't': 1,
   'U': 1, 'u': 1,
   'V': 1, 'v': 1,
   'W': 1, 'w': 1,
   'X': 1, 'x': 1,
   'Y': 1, 'y': 1,
   'Z': 1, 'z': 1
  })
