#Problem 1: BFS using queue and iterative approach
def BFS(TREE):
    q = []
    res = []
    q.append(TREE)
    while q:
        curr = q.pop(0)
        if not isinstance(curr, tuple):
            res.append(curr)
            continue
        for elem in curr:
            if isinstance(elem, tuple):
                q.append(elem)
            else:
                res.append(elem)
    return tuple(res)

#Problem 2: DFS using recursion
def DFS(TREE):
    res = []
    if not isinstance(TREE, tuple):
        res.append(TREE)
        return tuple(res) 
    for elem in TREE:
        if not isinstance(elem, tuple):
            res.append(elem)
            continue
        res = res + list(DFS(elem))
    return tuple(res)

def DFID(TREE, D):
    res = []
    if not isinstance(TREE, tuple):
        res.append(TREE)
        return tuple(res)
    curr = TREE
    for i in range(D):
        temp = []
        next = []
        for elem in reversed(curr):
            if not isinstance(elem, tuple):
                temp.append(elem)
                next = list(elem) + next
            else:
                next = list(elem) + next
        res += temp
        curr = next
    return tuple(res)

#Problem 3: 

# These functions implement a depth-first solver for the homer-baby-dog-poison
# problem. In this implementation, a state is represented by a single tuple
# (homer, baby, dog, poison), where each variable is True if the respective entity is
# on the west side of the river, and False if it is on the east side.
# Thus, the initial state for this problem is (False False False False) (everybody
# is on the east side) and the goal state is (True True True True).

# The main entry point for this solver is the function DFS_SOL, which is called
# with (a) the state to search from and (b) the path to this state. It returns
# the complete path from the initial state to the goal state: this path is a
# list of intermediate problem states. The first element of the path is the
# initial state and the last element is the goal state. Each intermediate state
# is the state that results from applying the appropriate operator to the
# preceding state. If there is no solution, DFS_SOL returns [].
# To call DFS_SOL to solve the original problem, one would call
# DFS_SOL((False, False, False, False), [])
# However, it should be possible to call DFS_SOL with any intermediate state (S)
# and the path from the initial state to S (PATH).

# First, we define the helper functions of DFS_SOL.

# FINAL_STATE takes a single argument S, the current state, and returns True if it
# is the goal state (True, True, True, True) and False otherwise.
def FINAL_STATE(S):
    return all(x is True for x in S)


# NEXT_STATE returns the state that results from applying an operator to the
# current state. It takes two arguments: the current state (S), and which entity
# to move (A, equal to "h" for homer only, "b" for homer with baby, "d" for homer
# with dog, and "p" for homer with poison).
# It returns a list containing the state that results from that move.
# If applying this operator results in an invalid state (because the dog and baby,
# or poisoin and baby are left unsupervised on one side of the river), or when the
# action is impossible (homer is not on the same side as the entity) it returns [].
# NOTE that NEXT_STATE returns a list containing the successor state (which is
# itself a tuple)# the return should look something like [(False, False, True, True)].
def NEXT_STATE(S, A):
    h, b, d, p = S
    if A == 'h':
        new_state = (not h, b, d, p)
    elif A == 'b':
        if h != b:
            return []
        new_state = (not h, not b, d, p)
    elif A == 'd':
        if h != d:
            return []
        new_state = (not h, b, not d, p)
    elif A == 'p':
        if h != p:
            return []
        new_state = (not h, b, d, not p)
    else:
        return []
    # Safety check 
    nh, nb, nd, np = new_state
    if (nb == nd and nh != nb) or (nb == np and nh != nb):
        return []
    return [new_state]

        
# SUCC_FN returns all of the possible legal successor states to the current
# state. It takes a single argument (S), which encodes the current state, and
# returns a list of each state that can be reached by applying legal operators
# to the current state.
def SUCC_FN(S):
    actions = ['h', 'b', 'd', 'p']
    next = []
    for a in actions:
        if NEXT_STATE(S, a):
            next = next + NEXT_STATE(S, a)
    return next
 


# ON_PATH checks whether the current state is on the stack of states visited by
# this depth-first search. It takes two arguments: the current state (S) and the
# stack of states visited by DFS (STATES). It returns True if S is a member of
# STATES and False otherwise.
def ON_PATH(S, STATES):
    return S in set(STATES)


# MULT_DFS is a helper function for DFS_SOL. It takes two arguments: a list of
# states from the initial state to the current state (PATH), and the legal
# successor states to the last, current state in the PATH (STATES). PATH is a
# first-in first-out list of states# that is, the first element is the initial
# state for the current search and the last element is the most recent state
# explored. MULT_DFS does a depth-first search on each element of STATES in
# turn. If any of those searches reaches the final state, MULT_DFS returns the
# complete path from the initial state to the goal state. Otherwise, it returns
# [].
def MULT_DFS(STATES, PATH):
    if FINAL_STATE(PATH[-1]): #We've reached the goal state, return complete path
        return PATH
    if not STATES:
        return []
    else: #Keep searching
        for state in STATES:
            res = DFS_SOL(state, PATH[:])
            if res:
                return res
        return []


# DFS_SOL does a depth first search from a given state to the goal state. It
# takes two arguments: a state (S) and the path from the initial state to S
# (PATH). If S is the initial state in our search, PATH is set to []. DFS_SOL
# performs a depth-first search starting at the given state. It returns the path
# from the initial state to the goal state, if any, or [] otherwise. DFS_SOL is
# responsible for checking if S is already the goal state, as well as for
# ensuring that the depth-first search does not revisit a node already on the
# search path (i.e., S is not on PATH).
def DFS_SOL(S, PATH):
    if FINAL_STATE(S):
        return PATH + [S]
    elif ON_PATH(S, PATH):
        return []
    else:
        PATH.append(S)
        successors = SUCC_FN(S)
        result = MULT_DFS(successors, PATH[:])
        PATH.pop()
        return result

if __name__ == "__main__":
    assert BFS("ROOT") == ('ROOT',)
    assert BFS(((("L", "E"), "F"), "T")) == ('T', 'F', 'L', 'E')
    assert BFS(("R", ("I", ("G", ("H", "T"))))) == ('R', 'I', 'G', 'H', 'T')
    assert BFS((("A", ("B",)), ("C",), "D")) == ('D', 'A', 'C', 'B')
    assert BFS(("T", ("H", "R", "E"), "E")) == ('T', 'E', 'H', 'R', 'E')
    assert BFS(("A", (("C", (("E",), "D")), "B"))) == ('A', 'B', 'C', 'D', 'E')

    print("All test cases for BFS passed!")

    assert DFS("ROOT") == ('ROOT',)
    assert DFS(((("L", "E"), "F"), "T")) == ('L', 'E', 'F', 'T')
    assert DFS(("R", ("I", ("G", ("H", "T"))))) == ('R', 'I', 'G', 'H', 'T')
    assert DFS((("A", ("B",)), ("C",), "D")) == ('A', 'B', 'C', 'D')
    assert DFS(("T", ("H", "R", "E"), "E")) == ('T', 'H', 'R', 'E', 'E')
    assert DFS(("A", (("C", (("E",), "D")), "B"))) == ('A', 'C', 'E', 'D', 'B')

    print("All test cases for DFS passed!")

    assert DFID("ROOT", 0) == ('ROOT',)
    assert DFID(((("L", "E"), "F"), "T"), 3) == ('T', 'T', 'F', 'T', 'F', 'E', 'L')
    assert DFID(("R", ("I", ("G", ("H", "T")))), 4) == ('R', 'I', 'R', 'G', 'I', 'R', 'T', 'H', 'G', 'I', 'R')
    assert DFID(((("A", ("B",)), ("C",), "D")), 3) == ('D', 'D', 'C', 'A', 'D', 'C', 'B', 'A')
    assert DFID(("T", ("H", "R", "E"), "E"), 2) == ('E', 'T', 'E', 'E', 'R', 'H', 'T')
    assert DFID(("A", (("C", (("E",), "D")), "B")), 5) == ('A', 'B', 'A', 'B', 'C', 'A', 'B', 'D', 'C', 'A', 'B', 'D', 'E', 'C', 'A')

    print("All test cases for DFID passed!")

    print(DFS_SOL((False, False, False, False), []))