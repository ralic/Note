# coding=utf-8
"""
Create a rectagular grid and iterate through 
a subset of its cells in a specified direction
网格的各种撸法
"""


GRID_HEIGHT = 4
GRID_WIDTH = 4

# 随便创建一个网格，赋予初值
EXAMPLE_GRID = [[row + col for col in range(GRID_WIDTH)]
                for row in range(GRID_HEIGHT)]


def traverse_grid(start_cell, direction, num_steps):
    """
    start_cell:起点
    direction：方向
    num_steps:从起点的某个方向出发的步长
    """
    for step in range(num_steps):
        srow = start_cell[0] + step * direction[0]
        scol = start_cell[1] + step * direction[1]
        print "Processing cell", (srow, scol),
        print "with value", EXAMPLE_GRID[srow][scol]


def run_example():
    """
    Run several example calls of traverse_grid()
    """
    print "Print out values in grid"
    for row in range(GRID_HEIGHT):
        print EXAMPLE_GRID[row]
    print
    
    print "第一行，由左到右"
    traverse_grid((0, 0), (0, 1), GRID_WIDTH)
    print
    
    print "第二列，由上到下"
    traverse_grid((0, 1), (1, 0), GRID_HEIGHT)
    print
    
    print "第二列，由下到上"
    traverse_grid((GRID_HEIGHT - 1, 1), (-1, 0), GRID_HEIGHT)
    print
    
    print "diagonal对角线左上->右下"
    traverse_grid((0, 0), (1, 1), min(GRID_WIDTH, GRID_HEIGHT))
    print 
    
    print "diagonal对角线右下->左上"
    traverse_grid((GRID_HEIGHT - 1, GRID_WIDTH - 1), (-1, -1), min(GRID_WIDTH, GRID_HEIGHT))
    print 
    
    print "diagonal对角线左下->右上 "
    traverse_grid((GRID_HEIGHT - 1, 0), (-1, 1), min(GRID_WIDTH, GRID_HEIGHT))
    print 
    
    print "diagonal对角线右上->左下"
    traverse_grid((0, GRID_WIDTH-1), (1, -1), min(GRID_WIDTH, GRID_HEIGHT))
    print 
run_example()


