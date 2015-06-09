import argparse
import datetime
parser = argparse.ArgumentParser()
parser.add_argument("square", type=int,
help="display a square of a given number")
parser.add_argument("-v", "--verbosity", type=str,
help="increase output verbosity")
args = parser.parse_args()
answer = args.square**2
# if args.verbosity == 2:
#     print "the square of {} equals {}".format(args.square, answer)
# elif args.verbosity == 1:
#     print "{}^2 == {}".format(args.square, answer)
# else:
print args
print answer


def es_argsparse():
    parser = argparse.ArgumentParser(description='es args')
    parser.add_argument("-s", "--stime", help="the start time")
    parser.add_argument("-e", "--etime", help="the end time")
    args = parser.parse_args()
    args.stime = tuple([int(i) for i in args.stime.split(',')])
    args.etime = tuple([int(i) for i in args.etime.split(',')])
    return args
