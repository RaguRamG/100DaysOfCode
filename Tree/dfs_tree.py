
#You are given a Node class that has a name and an array of optional children Nodes. 
#When put together, Nodes form a simple tree-like structure. Implement the depthFirstSearch method on the Node class, 
#which takes in an empty array, traverses the tree using the Depth-first Search approach 
#(specifically navigating the tree from left to right), stores all the of the 
#Nodes' names in the input array, and returns it.


class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self
    
    def depthFirstSearch(self, array):
        array.append(self.name)
        for child in self.children:
            child.depthFirstSearch(array)
        #print self.name
        return array

if __name__ == '__main__':
    n = Node('A')
    n.addChild('B')
    n.addChild('C')
    n.children[0].addChild('E')
    n.children[0].addChild('F')
    #print n.children[0].name
    n.depthFirstSearch([])