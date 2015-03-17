class MyStack(object):
    def __init__(self, maxsize):
        self._maxsize = maxsize
        self._top = -1
        self._elements = []

    def push(self, element):
        if len(self._elements) < self._maxsize:
            self._top += 1
            self._elements.append(element)
        else:
            print "Full"

    def pop(self):
        if self._top > -1:
            element = self._elements[self._top]
            del self._elements[self._top]
            self._top -= 1
            return element

    def get_top(self):
        return self._elements[self._top] if self._top >= 0 else None

    def __str__(self):
        result = []
        for i in self._elements[::-1]:
            result.append("--%d" % i)
        return "\n".join(result)

if __name__ == '__main__':
    st = MyStack(3)
    st.push(10)
    st.push(9)
    st.push(8)
    print st
    st.pop()
    st.pop()
    print st.get_top()
    st.pop()
    st.pop()
    print st.get_top()
    print st