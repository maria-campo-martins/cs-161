
#Q1: Computes n-th padovan number using recursion. 
def PAD(n): 
    if n == 0 or n == 1 or n == 2:
        return 1
    else:
        return PAD(n-1) + PAD(n-2)

#Q2: Computes number of additions required to compute n-th padovan number using recursion.
def SUMS(n):
    if n == 0 or n == 1 or n == 2:
        return 0
    else:
        return 1 + SUMS(n-1) + SUMS(n-2)    

#Q3: Recursively iterate through each subtree (tuple) to build anonymized tree. 
def ANON(TREE):
    res = []
    if not isinstance(TREE, tuple):
        return '?'
    for elem in TREE:
        if isinstance(elem, tuple):
            temp = ANON(elem)
        else:
            temp = '?'
        res.append(temp)
    return tuple(res)

#Q4: Compute height of tree by computing the maximum depth of all subtrees.  
def TREE_HEIGHT(TREE):
    res = 1
    if not isinstance(TREE, tuple):
        return 0
    for elem in TREE:
        if isinstance(elem, tuple):
            res = max(res, 1 + TREE_HEIGHT(elem))
    return res

#Q5: Postorder traversal of a tree by traversing left, right, and then center node, recursively. 
def TREE_ORDER(TREE):
    res = []
    if not isinstance(TREE, tuple):
        res.append(TREE)
    else:
        l, m, r = TREE
        res = TREE_ORDER(l) + TREE_ORDER(r) + TREE_ORDER(m)
    return tuple(res)

def run_tests():
    print('>>> ANON(42)')
    print(ANON(42))  # Expected: '?'
    print('>>> ANON("FOO")')
    print(ANON("FOO"))  # Expected: '?'
    print('>>> ANON((("L", "E"), "F"), "T")')
    print(ANON((((("L", "E"), "F"), "T"))))  # Expected: (((‘?’, ’?’), ’?’), ’?’)
    print('>>> ANON((5, "FOO", 3.1, -0.2))')
    print(ANON((5, "FOO", 3.1, -0.2)))  # Expected: ('?', '?', '?', '?')
    print('>>> ANON((1, ("FOO", 3.1), -0.2))')
    print(ANON((1, ("FOO", 3.1), -0.2)))  # Expected: ('?', ('?', '?'), '?')
    print('>>> ANON((((1, 2), ("FOO", 3.1)), ("BAR", -0.2)))')
    print(ANON((((1, 2), ("FOO", 3.1)), ("BAR", -0.2))))  # Expected: (((‘?’, ’?’), (’?’, ’?’)), (’?’, ’?’))
    print('>>> ANON(("R", ("I", ("G", ("H", "T")))))')
    print(ANON(("R", ("I", ("G", ("H", "T"))))))  # Expected: ('?', ('?', ('?', ('?', '?'))))

    print('>>> TREE_HEIGHT(1)')
    print(TREE_HEIGHT(1))  # Expected: 0
    print('>>> TREE_HEIGHT((5, "FOO", 3.1, -0.2))')
    print(TREE_HEIGHT((5, "FOO", 3.1, -0.2)))  # Expected: 1
    print('>>> TREE_HEIGHT((1, ("FOO", 3.1), -0.2))')
    print(TREE_HEIGHT((1, ("FOO", 3.1), -0.2)))  # Expected: 2
    print('>>> TREE_HEIGHT(("R", ("I", ("G", ("H", "T")))))')
    print(TREE_HEIGHT(("R", ("I", ("G", ("H", "T"))))))  # Expected: 4

    print('>>> TREE_ORDER(42)')
    print(TREE_ORDER(42))  # Expected: (42,)
    print('>>> TREE_ORDER(((1, 2, 3), 7, 8))')
    print(TREE_ORDER(((1, 2, 3), 7, 8)))  # Expected: (1, 3, 2, 8, 7)
    print('>>> TREE_ORDER(((3, 7, 10), 15, ((16, 18, 20), 30, 100)))')
    print(TREE_ORDER(((3, 7, 10), 15, ((16, 18, 20), 30, 100))))  # Expected: (3, 10, 7, 16, 20, 18, 100, 30, 15)

if __name__ == "__main__":
    run_tests()

