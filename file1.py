import sys
from random import randrange, shuffle
from tkinter import *
from tkinter.simpledialog import askstring

sys.setrecursionlimit(100000)

BOTTOM_WALL = 0
RIGHT_WALL = 1
E,S,W,N = 0, 1, 2, 3
DIRECTION = [(0,1),(1,0),(0,-1),(-1,0)]
  
class Maze:
    def __init__(self, row, col):
        self.row , self.col = row, col
        self.maze = [[[True, True, False] for c in range(col)] for r in range(row)]
        self.makepath(randrange(row), randrange(col))
  
    def makepath(self, r, c, direct = None):#随机拆墙
        global maze
        maze = self.maze
 
        maze[r][c][2] = True
 
        if direct == N: maze[r][c][BOTTOM_WALL] = False
        if direct == S: maze[r-1][c][BOTTOM_WALL] = False
        if direct == W: maze[r][c][RIGHT_WALL] = False
        if direct == E: maze[r][c-1][RIGHT_WALL] = False
  
        fangxiang = []
        if r > 0: fangxiang.append(N)
        if r < self.row - 1: fangxiang.append(S)
        if c > 0: fangxiang.append(W)
        if c < self.col - 1: fangxiang.append(E)
  
        shuffle(fangxiang)
  
        for i in fangxiang:
 
            e, f = DIRECTION[i]
 
            if maze[r+e][c+f][2] == False:
                self.makepath(r+e, c+f, i)
  
    def draw(self, size, canvas):#画出整个迷宫
        d = 5
 
        canvas.config(width = d*2+self.col*size, height = d*2+self.row*size)  #设置一个或多个选项
        line = canvas.create_line
        line(d,d,(self.col-1)*size+5,d)
        line(d,d,d,(self.row-1)*size+5)
       
 
        for r in range(self.row):
            for c in range(self.col):
 
                if self.maze[r][c][BOTTOM_WALL]:
                    line(c*size+d, (r+1)*size+d, (1+c)*size+d, (r+1)*size+d)
 
                if self.maze[r][c][RIGHT_WALL]:
                    line((c+1)*size+d, r*size+d, (c+1)*size+d, (r+1)*size+d)
width = 400
height = 400
king = Tk()
king.title("maze")
king.geometry("+550+250")
canvas = Canvas(king,bg='orange')
canvas.grid(row=1,column=1)