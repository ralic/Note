# coding=utf-8
"""
Clone of 2048 game.
"""
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# 表示(row, col)的方向偏移，比如UP、DOWN，上下移动则固定列，行的方向则进行偏移
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}


def merge(line):
    """
    2048合并方案
    """
    # save the line length
    length = len(line)
    # 过滤列表中的零
    filter_func = lambda x: x != 0
    # 将第一次过滤的结果存储起来，等待合并
    result = filter(filter_func, line)
    # 记录当前方块的位置
    index = 0
    # 合并的规则：相邻的方块才能合并
    while index <= len(result):
        # 一旦index指向最后一个方块，那么合并终止
        if index + 1 >= len(result):
            break
        # 当index指向的方块与其相邻的方块相等，则立即合并，结果保存当前方块，被合并的方块结果置零，index指向下一个非零块
        if result[index] == result[index + 1]:
            result[index] *= 2
            result[index+1] = 0
            index += 2
        # 不相等，则直接指向下一个非零块
        else:
            index += 1
    # 再次过滤为零的方块
    result = filter(filter_func, result)
    # 将result后续填充零，使其长度与给定列表line的长度一致
    result += [0] * (length - len(result))
    return result


class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        # 注意私有变量前加下划线
        self._height = grid_height  # 高度，行
        self._width = grid_width    # 宽度，列
        self._grid = None
        self.reset()

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        # 初始化游戏方格，默认填充0，
        self._grid = [[i*j*0 for i in range(self._width)] for j in range(self._height)]
        self.new_tile()
        self.new_tile()

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        grid_str = ""
        for row in self._grid:
            grid_str += str(row) + "\n"
        return grid_str

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        # replace with your code
        return self._height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        # replace with your code
        return self._width

    def move(self, direction):
        """
        核心函数：实现移动、合并、新增方块
        """
        # 确定移动方位的
        start_direction = OFFSETS[direction]
        # 根据移动的方位，确定按行或按列合并的长度
        # 比如在3*4的grid中，按照列来合并，总共要合并4列（此时行保持不变）
        num_steps = self._width if start_direction[0] == 0 else self._height
        # 生成方块聚合的起点
        if direction == UP:
            # 向上移动，则保持特定行不变，列数逐步递增（生成与列数相等的起点）
            indicates = [(0, col) for col in range(self._width)]
        elif direction == DOWN:
            # 向下移动，保持特定行不变，列数亦逐步递增
            indicates = [(self._height-1, col) for col in range(self._width)]
        elif direction == LEFT:
            # 向左移动，保持特定列不变，行数逐步递增
            indicates = [(row, 0) for row in range(self._height)]
        else:
            # 向右移动，保持特定列不变，行数逐步递增
            indicates = [(row, self._width - 1) for row in range(self._height)]
        # 遍历每个起始位置
        for indicate in indicates:
            # 待合并列表
            wait_merge_list = []
            # 取出相对起始位置，特定方向的每个方块，加入待合并列表
            for step in range(num_steps):
                # 计算相对起始位置的行、列下标
                row = indicate[0] + step * start_direction[0]
                col = indicate[1] + step * start_direction[1]
                wait_merge_list.append(self._grid[row][col])
            merge_list = merge(wait_merge_list)
            # 合并之后，将对应位置的各值进行重新赋值
            for step in range(num_steps):
                row = indicate[0] + step * start_direction[0]
                col = indicate[1] + step * start_direction[1]
                self._grid[row][col] = merge_list[step]
        self.new_tile()

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        # get 2 or 4
        num = 2 if random.randint(1, 101) <= 90 else 4
        # select a empty indicate
        zero_zone = [(row, col) for row in range(len(self._grid)) for col in range(len(self._grid[0]))
                     if self._grid[row][col] == 0]
        # 如果不存在空的格子，那么return掉
        if not zero_zone:
            return
        # 否则随机一个格子并赋值
        select = random.choice(zero_zone)
        self._grid[select[0]][select[1]] = num

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        # replace with your code
        return self._grid[row][col]


if __name__ == '__main__':
    obj = TwentyFortyEight(4, 5)
    obj.set_tile(0, 0, 8)
    obj.set_tile(0, 1, 16)
    obj.set_tile(0, 2, 8)
    obj.set_tile(0, 3, 16)
    obj.set_tile(0, 4, 8)
    print obj
    obj.set_tile(1, 0, 16)
    obj.set_tile(1, 1, 8)
    obj.set_tile(1, 2, 16)
    obj.set_tile(1, 3, 8)
    obj.set_tile(1, 4, 16)
    print obj
    obj.set_tile(2, 0, 8)
    obj.set_tile(2, 1, 16)
    obj.set_tile(2, 2, 8)
    obj.set_tile(2, 3, 16)
    obj.set_tile(2, 4, 8)
    print obj
    obj.set_tile(3, 0, 16)
    obj.set_tile(3, 1, 8)
    obj.set_tile(3, 2, 16)
    obj.set_tile(3, 3, 8)
    obj.set_tile(3, 4, 16)
    print obj
    obj.move(UP)  # result：[[8, 16, 8, 16, 8], [16, 8, 16, 8, 16], [8, 16, 8, 16, 8], [16, 8, 16, 8, 16]]

