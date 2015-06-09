import optparse
import sys
parser = optparse.OptionParser()

parser.add_option('-t', '--type', dest='tp')
parser.add_option('-n', '--name', dest='name')
options, remainder = parser.parse_args()
print "type:", options.tp
print "name :", options.name
print "remainder :", remainder