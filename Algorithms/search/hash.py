# coding=utf-8
class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size     # 哈希key
        self.data = [None] * self.size      # 哈希value

    def hashfunction(self, key, size):
        return key % size

    def rehash(self, oldhash, size):
        return (oldhash + 1) % size

    def put(self, key, value):
        hashvalue = self.hashfunction(key, len(self.slots))
        # 若key槽为None，那么直接设置slot和data对应hashvalue的键值
        if self.slots[hashvalue] is None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = value
        else:
            # slot对应的hashvalue位置与key值相等，则表明是对data对应位置的值进行替换
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = value
            else:
                nextshot = self.rehash(hashvalue, len(self.slots))
                while self.slots[nextshot] is not None and self.slots[nextshot] != key:
                    nextshot = self.rehash(nextshot, len(self.slots))
                if self.slots[nextshot] is None:
                    self.slots[nextshot] = key
                    self.data[nextshot] = value
                else:
                    self.data[nextshot] = value

    def get(self, key):
        startslot = self.hashfunction(key, len(self.slots))
        data = None
        stop = False
        found = False
        position = startslot
        while self.slots[position] is not None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == startslot:
                    stop = True
        return data

    # 拦截“[]”的设置和获取操作
    def __getitem__(self, item):
        return self.get(item)

    def __setitem__(self, key, value):
        self.put(key, value)

