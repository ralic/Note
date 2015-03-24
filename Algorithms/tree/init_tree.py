class Tree(object):
    def __init__(self, index, leftchild, rightchild):
        self.index = index
        self.leftchild = leftchild
        self.rightchild = rightchild

    def create_tree(self, node_list):
        pass

    def select_root(self, node_list):
        root_index = 0
        for index in range(1, len(node_list)):
            if node_list[index][1] == root_index or node_list[index][0] == root_index:
                root_index = index
        return node_list[root_index]

node_tuple = [(1, None), (None, None), (0, None), (2, 7),
              (None, None), (None, None), (5, None), (4, 6)]


for node in node_tuple:

    if node[0] or node[1]:
        continue