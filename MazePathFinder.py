import pygame
import math
from queue import PriorityQueue

WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("A* Path Finding Algorithm") 

RED = (255, 0, 0) #red then it is closed
GREEN = (0, 255, 0) #if the color is green then it is open
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255) #if the color is white then it is unvisited.
BLACK = (0, 0, 0) #if the color is black then it is a wall and we cannot move to that spot.
PURPLE = (128, 0, 128) #if the color is purple then it is the path that we have found from the start to the end.
ORANGE = (255, 165 ,0) #if the color is orange then it is the start spot.
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208) #if the color is turquoise then it is the end spot.

class Spot:
    # we need to track how this different nodes that are in our grid.
    #Thi is a huge gride like 50 by 50, the spot or node is the individual square in the grid and it hold a value of its position and its color and its neighbors and so on.
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width # we need to track the corridantion of the spot in the grid, so we can draw it on the screen. we need to know where to draw it. so we need to know the x and y coordinate of the spot. the x coordinate is the row number multiplied by the width of the spot, and the y coordinate is the column number multiplied by the width of the spot.
        self.y = col * width #
        self.color = WHITE  # default color
        self.neighbors = [] # we need to track the neighbors of the spot, so we can check if we can move to that spot or not. we need to check if the spot is a wall or not, if it is a wall we cannot move to that spot. if it is not a wall we can move to that spot. so we need to track the neighbors of the spot.
        self.width = width
        self.total_rows = total_rows # we need to track the total number of rows in the grid, so we can check if we are at the edge of the grid or not. if we are at the edge of the grid we cannot move to that spot.

    def get_pos(self):
        # this function is used to get the position of the spot in the grid, so we can use it to check if we are at the end of the grid or not. 
        # we can also use it to check if we are at the start of the grid or not.
        return self.row, self.col
    
    def is_closed(self):
        # closed means that we have already visited this spot 
        # and we don't want to visit it again. 
        return self.color == RED
    
    def is_open(self):
        return self.color == GREEN
    
    def is_barrier(self): # what its blocking us from moving to that spot, we cannot move to that spot if it is a barrier.
        return self.color == BLACK
    
    def is_start(self):
        return self.color == ORANGE
    
    def is_end(self):
        return self.color == TURQUOISE


# we need to make the spot closed, open, barrier, start, end and path. 
# we need to change the color of the spot to indicate that it is closed, open, barrier, start, end and path.
# this actually changes the color of the spot on the screen, so we can see it visually.

    def reset(self):
        self.color = WHITE

    def make_closed(self):
        self.color = RED

    def make_open(self):
        self.color = GREEN

    def make_barrier(self):
        self.color = BLACK

    def make_start(self):
        self.color = ORANGE

    def make_end(self):
        self.color = TURQUOISE

    def make_path(self):
        self.color = PURPLE

    def draw(self, win): # where do we wanna draw the spot
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width)) 
        # we need to draw a rectangle for each spot, so we need to know the x and y coordinate of the spot, and the width of the spot.

    def update_neighbors(self, grid):
        pass

    def __lt__(self, other): #lt = less than
        # this is a function that is used to compare two spots, so we can use it in the priority queue. 
        # we need to compare the f score of the two spots, 
        # so we can determine which spot is closer to the end spot.
        return False


# h function
def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)

