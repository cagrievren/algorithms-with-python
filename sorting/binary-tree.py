# The struct of tree is created.
class Tree:
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None
# It adds empty trees to left and right, and assigns data to given node.
def addLeft(root: Tree, data):
    root.data = data
    root.right = Tree()
    root.left = Tree()
# It adds empty trees to left and right, and assigns data to given node.   
def addRight(root: Tree, data):
    root.data = data
    root.right = Tree()
    root.left = Tree()
# Iterator iterates by value of data on tree.
# If the node data doesn't exists, it invokes addLeft() or addRight() methods by bigger or not than given data. 
def addToBinaryTree (root, data):
    temp = root
    onceki = root.data
    while temp.data:
        onceki = temp.data
        if data >  temp.data:
            temp = temp.right
        else:
            temp = temp.left
    if data > onceki:
        addRight(temp, data)
    else:
        addLeft(temp, data)

array = [74, 81, 1, 42, 5, 3, 41, 72, 71, 37, 51, 33, 15, 92, 17, 93, 52, 54]
# We need to assign a root and than we can add a value to tree.
root = Tree()
root.data = 53
root.left = Tree()
root.right = Tree()
for i in range(0, len(array)):
    addToBinaryTree(root, array[i]) # Yorum satırı eklendi
print(root.right.right.right.data)