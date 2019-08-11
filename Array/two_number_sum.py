#Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum. 
#If any two numbers in the input array sum up to the target sum, 
#the function should return them in an array, in sorted order. 
#If no two numbers sum up to the target sum, the function should return an empty array. 
#Assume that there will be at most one pair of numbers summing up to the target sum.
#Sample input: [3, 5, -4, 8, 11, 1, -1, 6], 10
#Sample output: [-1, 11]
def twoNumberSum(array, targetSum):
    output = []
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i]+array[j] == targetSum:
                if array[i]<array[j]:
                    output.append(array[i])
                    output.append(array[j])
                else:
                    output.append(array[j])
                    output.append(array[i])
    return output
                


if __name__ == '__main__':
    tsum = 10
    array = [3, 5, -4, 8, 11, 1, -1, 6]
    out = twoNumberSum(array, tsum)
    print out