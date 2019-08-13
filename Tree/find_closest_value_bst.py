#
#You are given a BST data structure consisting of BST nodes. 
#Each BST node has an integer value stored in a property called "value" and 
#two children nodes stored in properties called "left" and "right," respectively. 
#A node is said to be a BST node if and only if it satisfies the BST property: 
#its value is strictly greater than the values of every node to its left; 
#its value is less than or equal to the values of every node to its right; 
#and both of its children nodes are either BST nodes themselves or None (null) values. 
#You are also given a target integer value; write a function that finds the closest 
#value to that target value contained in the BST. Assume that there will only be one closest value.


class tree(object):
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

def findClosestValue(t, target, closest):
    if t is None:
        return closest
    if t.value == target:
        return t.value
    if abs(target-closest) > abs(target-t.value):
        closest = t.value
    if target < t.value:
        return findClosestValue(t.left, target, closest)
    elif target > t.value:
        return findClosestValue(t.right, target, closest)
    else:
        return t.value

def findClosestValueInBst(t, target):
    return findClosestValue(t, target, float('inf'))
                   

if __name__ == '__main__':
    t = tree(10)
    t.left = tree(5)
    t.right = tree(15)
    t.left.left = tree(2)
    t.left.right = tree(5)
    t.right.left = tree(13)
    t.right.right = tree(22)
    t.left.left.left = tree(1)
    t.right.left.left = tree(14)
    print t.left.value
    print findClosestValueInBst(t, 12)
    
