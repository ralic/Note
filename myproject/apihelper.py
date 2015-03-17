import os
import sys
from UserDict import UserDict


def info(obj, spacing=10, collapse=1):
    """
    Print methods and doc strings.Takes module, class, list, dictionary, or string.
    """
    methodlist = [method for method in dir(obj) if callable(getattr(obj, method))]
    processfunc = collapse and (lambda s: " ".join(s.split())) or (lambda s: s)
    print "\n".join(["%s %s" % (method.ljust(spacing), processfunc(str(getattr(obj, method).__doc__)))
                     for method in methodlist])


def stripnulls(data):
    return data.replace("\00", "").strip()


class FileInfo(UserDict):
    """hello"""
    def __init__(self, filename=None):
        UserDict.__init__(self)
        self.data["name"] = filename
