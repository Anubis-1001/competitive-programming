def pathSumAux(root, targetSum, c_sum):
    if not root:
        return []
    if c_sum+root.val == targetSum and root.left==None and root.right==None:
        return [[root.val]]
    c_sum+=root.val
    left=[]
    right=[]
    result=[]
    right=pathSumAux(root.right, targetSum, c_sum)
    left=pathSumAux(root.left, targetSum, c_sum)
    if len(right) > 0:
        for r in right:
            r.insert(0, root.val)
        result+=right
    if len(left) > 0:
        for l in left:
            l.insert(0, root.val)
        result+=left

    return result

