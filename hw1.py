
#Q1: Computes n-th padovan number using memoization. 
def PAD(n): 
    if n == 0 or n == 1 or n == 2:
        return 1
    memo = [1] * (n+1)
    for i in range(3, n+1):
        memo[i] = memo[i-2] + memo[i-3]
    return memo[n]

#Q2: Computes number of additions required to compute n-th padovan number using memoization.
def SUMS(n):
    if n == 0 or n == 1 or n == 2:
        return 0
    memo = [0] * (n+1)
    for i in range(3, n+1):
        memo[i] = 1 + memo[i-2] + memo[i-3]
    return memo[n]  

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

