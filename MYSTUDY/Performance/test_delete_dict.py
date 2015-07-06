mydict = {
    "hello": 1,
    "world": 1,
    "my": 2,
    "name": 3,
    "is": 4,
    "hi": 5
}

def update_dict(dct):
    dct_cp = dct.copy()
    return {key: value for key, value in dct_cp.items() if key in ["hello", "my", "hi"]}


def del_dict(dct):
    dct_cp = dct.copy()
    del dct_cp["world"]
    del dct_cp["name"]
    del dct_cp["is"]
    return dct

@profile
def test_range():
    for i in range(10000):
        i += 1

@profile
def test_xrange():
    for index, i in enumerate(range(10000)):
        i += 1

if __name__ == '__main__':
    test_range()
    test_xrange()