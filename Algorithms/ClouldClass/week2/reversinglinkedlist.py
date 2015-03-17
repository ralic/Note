class Node(object):
    def __init__(self, address, data, node=None):
        self.data = data
        self.address = address
        self.next = node

    def create_node(self, nodelist):
        while nodelist:
            result = filter(lambda address: address == self.next.address, nodelist)


    def __str__(self):
        print self.next
        if self.next is not None:
            return "%s %d %s" % (self.address, self.data, self.next.address)
        else:
            return "%s %d None" % (self.address, self.data)
if __name__ == '__main__':
    n1 = Node("00100", 6, None)
    l2 = Node("00000", 4, n1)
    print l2


