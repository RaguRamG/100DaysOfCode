def powerset(array, idx=None):
    if idx is None:
        idx = len(array) - 1
    elif idx < 0:
        return [[]]
    ele = array[idx]
    subsets = powerset(array, idx - 1)
    print subsets, "ele: ", ele
    for i in range(len(subsets)):
        currentSubset = subsets[i]
        subsets.append(currentSubset + [ele])
    return subsets


output = powerset([1, 2, 3, 4])
print output
