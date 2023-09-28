class Tree:
    def __init__(self, cargo, left=None, right=None):
        self.cargo = cargo
        self.left  = left
        self.right = right

    def __str__(self):
        return str(self.cargo)


def preorder_tree(tree):
    if tree == None: return
    print(tree.cargo, end=' ') 
    preorder_tree(tree.left)
    preorder_tree(tree.right)
	

def inorder_tree(tree):
    if tree == None: return
    inorder_tree(tree.left)
    print(tree.cargo, end=' ') 
    inorder_tree(tree.right)
	

def postorder_tree(tree):
    if tree == None: return
    postorder_tree(tree.left)
    postorder_tree(tree.right)
    print(tree.cargo, end=' ')	
	
tree = Tree('+', Tree('*',Tree('3'),Tree('A')),  Tree('/',Tree('B'),Tree('4')))
print("\n\nPreorder")
preorder_tree(tree)
print("\n\nInorder")
inorder_tree(tree)
print("\n\nPostorder")
postorder_tree(tree)
