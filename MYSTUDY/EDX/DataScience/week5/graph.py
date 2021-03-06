# coding=utf-8
# 6.00.2x Problem Set 5
# Graph optimization
#
# A set of data structures to represent graphs
#


class Node(object):
    def __init__(self, name):
        self.name = str(name)
    def getName(self):
        return self.name
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name
    def __eq__(self, other):
        return self.name == other.name
    def __ne__(self, other):
        return not self.__eq__(other)
    def __hash__(self):
        # Override the default hash method
        # Think: Why would we want to do this?
        return self.name.__hash__()


class Edge(object):
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest
    def __str__(self):
        return '{0}->{1}'.format(self.src, self.dest)


class Digraph(object):
    """
    A directed graph
    """
    def __init__(self):
        # A Python Set is basically a list that doesn't allow duplicates.
        # Entries into a set must be hashable (where have we seen this before?)
        # Because it is backed by a hashtable, lookups are O(1) as opposed to the O(n) of a list (nifty!)
        # See http://docs.python.org/2/library/stdtypes.html#set-types-set-frozenset
        self.nodes = set([])
        self.edges = {}
    def addNode(self, node):
        if node in self.nodes:
            # Even though self.nodes is a Set, we want to do this to make sure we
            # don't add a duplicate entry for the same node in the self.edges list.
            raise ValueError('Duplicate node')
        else:
            self.nodes.add(node)
            self.edges[node] = []
    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not(src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)
    def childrenOf(self, node):
        return self.edges[node]
    def hasNode(self, node):
        return node in self.nodes
    def __str__(self):
        res = ''
        for k in self.edges:
            for d in self.edges[str(k)]:
                res = '{0}{1}->{2}\n'.format(res, k, d)
        return res[:-1]


class WeightedDigraph(Digraph):
    def __init__(self):
        Digraph.__init__(self)

    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        totaldis = edge.getTotalDistance()
        outdoordis = edge.getOutdoorDistance()
        if not(src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        self.edges[src].append([dest, (totaldis, outdoordis)])

    def __str__(self):
        res = ''
        for s in self.edges:
            for d in self.edges[s]:
                res += '{0}->{1} ({2:.1f}, {3:.1f})\n'.format(s, d[0], d[1][0], d[1][1])
        return res[:-1]

    def addNode(self, node):
        if node in self.nodes:
            # Even though self.nodes is a Set, we want to do this to make sure we
            # don't add a duplicate entry for the same node in the self.edges list.
            pass
        else:
            self.nodes.add(node)
            self.edges[node] = []


class WeightedEdge(Edge):
    def __init__(self, src, dest, distance, outdoor):
        Edge.__init__(self, src, dest)
        self.distance = distance
        self.outdoor = outdoor

    def __str__(self):
        return '{0}->{1} ({2}, {3})'.format(self.src, self.dest, self.distance, self.outdoor)


    def getTotalDistance(self):
        return self.distance

    def getOutdoorDistance(self):
        return self.outdoor


def dfs(graph, start_node, end_node, path=None):
    if not path:
        path = []
    path = path + [start_node]
    print "Current dfs path:", path
    if start_node == end_node:
        return path
    for node in graph.childrenOf(start_node):
        if node not in path:
            newpath = dfs(graph, node, end_node, path)
            if newpath is not None:
                return newpath
    return None


def dfs_shortpath(graph, start_node, end_node, path=None, shortest=None):
    if not path:
        path = []
    path = path + [start_node]
    print "Current dfs path:", path
    if start_node == end_node:
        return path
    for node in graph.childrenOf(start_node):
        if node not in path:
            if shortest is None or len(path) < len(shortest):
                newpath = dfs(graph, node, end_node, path)
                if newpath is not None:
                    shortest = newpath
    return shortest


def bfs(graph, start_node, end_node, q=None):
    if not q:
        q = []
    initpath = [start_node]
    q.append(initpath)
    while len(q) != 0:
        print q
        # 出队
        tmppath = q.pop(0)
        lastnode = tmppath[-1]
        print 'Current dequened path:', tmppath
        if lastnode == end_node:
                return tmppath
        for node in graph.childrenOf(lastnode):
            if node not in tmppath:
                newpath = tmppath + [node]
                q.append(newpath)
    return None

if __name__ == '__main__':
    n0 = Node('ABC')
    n1 = Node('ACB')
    n4 = Node('CAB')
    n5 = Node('CBA')
    n2 = Node('BAC')
    n3 = Node('BCA')
    e1 = WeightedEdge(n0, n1, 1, 1)
    e2 = Edge(n0, n2)
    e3 = Edge(n1, n4)
    e5 = Edge(n4, n5)
    e6 = Edge(n2, n3)
    e4 = Edge(n3, n5)
    print e1
    g = Digraph()
    g.addNode(n0)
    g.addNode(n1)
    g.addNode(n2)
    g.addNode(n3)
    g.addNode(n4)
    g.addNode(n5)
    g.addEdge(e1)
    g.addEdge(e2)
    g.addEdge(e3)
    g.addEdge(e4)
    g.addEdge(e5)
    g.addEdge(e6)
    # print dfs(g, n0, n3)
    print dfs_shortpath(g, n0, n5)
    # print bfs(g, n0, n3)
