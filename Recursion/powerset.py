def powerset(array):
    subsets = [[]]
    for ele in array:
        for i in range(len(subsets)):
            currSubset = subsets[i] + [ele]
            subsets.append(currSubset)
    return subsets

output = powerset([1, 2, 3, 4])
print output
