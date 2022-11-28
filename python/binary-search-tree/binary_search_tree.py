class TreeNode:
    def __init__(self, data, left=None, right=None):
        #print("coming with data = ", data)
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return f'TreeNode(data={self.data}, left={self.left}, right={self.right})'


class BinarySearchTree:
    def __init__(self, tree_data):
        self.head = TreeNode(tree_data[0])
        self.all_data = tree_data

        for i in range(len(tree_data)-1):
            data = tree_data[i+1]
            parent = self.head
                        
            assigned :bool = False
            while not assigned:
                if int(data) <= int(parent.data):
                    if parent.left == None:
                        parent.left = TreeNode(data)
                        assigned = True
                    else:
                        parent = parent.left
                elif int(data) > int(parent.data):
                    if parent.right == None:
                        parent.right = TreeNode(data)
                        assigned = True
                    else:
                        parent = parent.right

            

    def data(self):
        return self.head

    def sorted_data(self):
        return sorted(self.all_data)
