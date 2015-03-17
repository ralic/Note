import sys
from pymongo import Connection
from pymongo.errors import ConnectionFailure


def main():
    try:
        c = Connection("localhost", 27017)
        print "Connection successfully!"
    except ConnectionFailure, e:
        sys.stderr.write("Could not connect to MongoDB: %s" % e)
        sys.exit(1)

if __name__ == '__main__':
    main()