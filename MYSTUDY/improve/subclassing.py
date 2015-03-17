# coding=utf-8
# 子类化内建类型


class DistinctError(Exception):
    pass


class MyField(dict):
    """继承自内建字典类型，不允许存在多个相同的键值"""
    def __setitem__(self, key, value):
        try:
            value_index = self.values().index(value)
            existing_key = self.keys()[value_index]
            if existing_key != key:
                raise DistinctError(("This value already exists for '%s'" % str(self[existing_key])))
        except ValueError:
            pass
        super(Field, self).__setitem__(key, value)

def testfield():
    my = Field()
    my['key'] = 'value'
    # 将会抛出异常
    my['other_key'] = 'value'


class MyList(list):
    __conn = None
    def __getitem__(self, offset):
        print "indexing %s at %s" % (self, offset)
        return list.__getitem__(self, offset - 1)

    def __private(self):
        print "I"


def testmylist():
    print list('abc')
    x = MyList("abc")
    print x
    print x[1]
    print x[3]

    x.append('spam')
    print x
    x.reverse()
    print x


class Field(dict):
    """Container of field metadata"""


class ItemMeta(type):

    def __new__(mcs, class_name, bases, attrs):
        fields = {}
        new_attrs = {}
        for n, v in attrs.iteritems():
            if isinstance(v, Field):
                fields[n] = v
            else:
                new_attrs[n] = v
        # 类名、父类、属性字典
        cls = super(ItemMeta, mcs).__new__(mcs, class_name, bases, new_attrs)
        print mcs, class_name, bases, attrs
        print cls.fields
        cls.fields = cls.fields.copy()
        cls.fields.update(fields)
        print cls.fields
        return cls


class DictItem(dict):
    fields = {}

    def __init__(self, *args, **kwargs):
        super(DictItem, self).__init__(*args, **kwargs)
        self._values = {}
        if args or kwargs:  # avoid creating dict for most common case
            for k, v in dict(*args, **kwargs).iteritems():
                self[k] = v

    def __getitem__(self, key):
        return self._values[key]

    def __setitem__(self, key, value):
        if key in self.fields:
            self._values[key] = value
        else:
            raise KeyError("%s does not support field: %s" %
                (self.__class__.__name__, key))

    def __delitem__(self, key):
        del self._values[key]

    def __getattr__(self, name):
        if name in self.fields:
            raise AttributeError("Use item[%r] to get field value" % name)
        raise AttributeError(name)

    def __setattr__(self, name, value):
        if not name.startswith('_'):
            raise AttributeError("Use item[%r] = %r to set field value" %
                (name, value))
        super(DictItem, self).__setattr__(name, value)

    def keys(self):
        return self._values.keys()

    def __repr__(self):
        return format(dict(self))

    def copy(self):
        return self.__class__(self)


class Item(DictItem):
    __metaclass__ = ItemMeta
    x = Field()
    y = Field()

if __name__ == '__main__':
    # testmylist()
    print Field()
    item = Item()