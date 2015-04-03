class BinaryTree(object):
    def __init__(self, root):
        self.key = root
        self.leftchild = None
        self.rightchild = None

    def insertleft(self, node):
        if self.leftchild is None:
            self.leftchild = BinaryTree(node)
        else:
            t = BinaryTree(node)
            t.leftchild = self.leftchild
            self.leftchild = t

    def insertright(self, node):
        if self.rightchild is None:
            self.rightchild = BinaryTree(node)
        else:
            t = BinaryTree(node)
            t.rightchild = self.rightchild
            self.rightchild = t

    def get_rightchild(self):
        return self.rightchild

    def get_leftchild(self):
        return self.leftchild

    def get_rootval(self):
        return self.key

    def set_rootval(self, value):
        self.key = value

if __name__ == '__main__':
    r = BinaryTree('a')
    print r.get_rootval(), r.get_leftchild(), r.get_rightchild()
    r.insertright('b')
    print r.get_rightchild()
    r.insertleft('c')
    print r.get_leftchild(), r.get_leftchild().get_rootval()