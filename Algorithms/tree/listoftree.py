# coding=utf-8
# 用列表来表示树
# a(b(d,e),c(f))
myTree = ['a',  # root
          ['b',  # left subtree
            ['d', [], []],
            ['e', [], []]
          ],
          ['c',  # right subtree
            ['f', [], []],
            []
          ]
]