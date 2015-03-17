# -*- coding: utf8 -*-
#
# python 生成器和闭包
#

import re


# def plural(noun):
# 	if re.search('[sxz]$', noun):
# 		return re.sub('$', 'es', noun)
# 	elif re.search('[^aeioudgkprt]h$', noun):
# 		return re.sub('$', 'es', noun)
# 	elif re.search('[^aeiou]y$', noun):
# 		return re.sub('y$', 'ies', noun)
# 	else:
# 		return noun + 's'
#
# def match_sxz(noun):
#     return re.search('[sxz]$', noun)
#
#
# def apply_sxz(noun):
#     return re.sub('$', 'es', noun)
#
#
# def match_h(noun):
#     return re.search('[^aeioudgkprt]h$', noun)
#
#
# def apply_h(noun):
#     return re.sub('$', 'es', noun)
#
#
# def match_y(noun):
#     return re.search('[^aeiou]y$', noun)
#
#
# def apply_y(noun):
#     return re.sub('y$', 'ies', noun)
#
#
# def match_default(noun):
#     return True
#
#
# def apply_default(noun):
#     return noun + 's'
#
# rules = ((match_sxz, apply_sxz),
#          (match_h, apply_h),
#          (match_y, apply_y),
#          (match_default, apply_default)
#          )

def build_match_and_apply_functions(pattern, search, replace):
    def matches_rule(word):
        return re.search(pattern, word)

    def apply_rule(word):
        return re.sub(search, replace, word)

    return (matches_rule, apply_rule)

patterns = \
    (
        ('[sxz]$',           '$',  'es'),
        ('[^aeioudgkprt]h$', '$',  'es'),
        ('(qu|[^aeiou])y$',  'y$', 'ies'),
        ('$',                '$',  's')
    )
rules = [build_match_and_apply_functions(pattern, search, replace)
         for (pattern, search, replace) in patterns]


def plural(noun):
    for matches_rule, apply_rule in rules:
        if matches_rule(noun):
            return apply_rule(noun)


class Test:
    def __init__(self, x):
        self.x = x

    def _private(self):
        print "private"

