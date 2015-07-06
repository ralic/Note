@profile
def test_range():
    return sum(range(1000000))

@profile
def test_xrange():
    a = list(xrange(1000000))
    return sum(a)

if __name__ == '__main__':
    test_range()
    test_xrange()