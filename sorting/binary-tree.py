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
def spanTree(root):
    if root.data:
        spanTree(root.left)
        print(root.data)
        spanTree(root.right)
    else:
        return 0
def findData(root: Tree,data):
    temp = root 
    while temp.data:
        if data > temp.data:
            temp = temp.right
        elif data< temp.data:
            temp = temp.left
        else:
            temp.data = findMostLeft(temp)
            return temp
    return 'bulunamadı'

def findMostLeft (root: Tree):
    onceki = root
    temp = root.left
    tempData = 0
    if temp.data:
        while temp.right.data:
            onceki = temp
            temp = temp.right
        tempData = temp.data
        if temp.left.data:
            onceki.right = temp.left
        else:
            temp.left = None
            temp.right = None
            temp.data = None
        return tempData
    else:
        print('Silinemedi')

array = [ 12, 48, 8, 26, 38, 62, 3, 10 , 13, 30, 35 , 42, 49, 18 , 32, 47,31]
# We need to assign a root and than we can add a value to tree.
root = Tree()
root.data = 33
root.left = Tree()
root.right = Tree()
for i in range(0, len(array)):
    addToBinaryTree(root, array[i])
#print(root.right.right.right.data)
print('BINARY TREE SORTED =>')
# print (type(findData(72))==str)
# deleteData(72)

aTree : Tree()
aTree = findData(root,62)
spanTree(root)
