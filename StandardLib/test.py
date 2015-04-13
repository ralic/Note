# coding=utf-8
from engin.main import bdcrawl
import json


def loadfile(filename):
    keywords = []
    with open(filename) as f:
        for words in f.readlines():
            keywords.append(words[:-1])
    return keywords


def json_result(keywords):
    print ".........START to ..........search..................."
    result = bdcrawl(keywords, count=5, types=None, headers={}, shop=None)
    return json.dumps(result)


def write_all_key(filename, objfile):
    count = 0
    with open(objfile, 'a') as f:
        try:
            for word in loadfile(filename):
                f.write(str(count) + "->" + word)
                f.write(json_result(word))
                f.write("\n----------------------\n")
                count += 1
        except:
            pass

if __name__ == '__main__':
    result = json_result(u'泡泡')
    write_all_key('hrs_keywords.txt', 'write.txt')
