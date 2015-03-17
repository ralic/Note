# coding=utf-8
# 运算符重载


# 索引和分片(slice)
class Indexer:
    data = []
    def __getitem__(self, index):
        return self.data[index] * 2

    def __setitem__(self, index, value):
        self.data.insert(index, value * 2)

    def __str__(self):
        return str(self.data)

if __name__ == '__main__':
    x = Indexer()
    x[0] = 1000
    x[1] = 20
    print x
