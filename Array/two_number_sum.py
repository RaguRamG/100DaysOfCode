#Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum. 
#If any two numbers in the input array sum up to the target sum, 
#the function should return them in an array, in sorted order. 
#If no two numbers sum up to the target sum, the function should return an empty array. 
#Assume that there will be at most one pair of numbers summing up to the target sum.
#Sample input: [3, 5, -4, 8, 11, 1, -1, 6], 10
#Sample output: [-1, 11]
def twoNumberSum(array, targetSum):
    output = []
    array.sort()
    i = 0
    n = len(array) - 1
    while i < n:
        tsum = array[i] + array[n]
        if tsum == targetSum:
            output.append(array[i])
            output.append(array[n])
            break #forgot to put break here
        elif tsum < targetSum:
            i += 1
        else:
            n -= 1
    return output
                


if __name__ == '__main__':
    tsum = 10
    array = [3, 5, -4, 8, 11, 1, -1, 6]
    out = twoNumberSum(array, tsum)
    print out