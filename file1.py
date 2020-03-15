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
size = askstring("迷宫难度", "迷宫的长和宽", initialvalue="25 25")
size = [int(x) for x in size.split()]
def drawCircle(self, x, y, r, **kwargs):
    return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
Maze(size[0],size[1]).draw(10,canvas)
yuan=drawCircle(canvas, 10,size[0]*10, 5, fill = "red")
yuan1=drawCircle(canvas, size[1]*10,10, 5, fill = "blue")
yuan2=drawCircle(canvas,10,size[0]*10, 5, fill = "yellow")
weizhi=[size[0]-1,0]
weizhi2=[size[0]-1,0]
def sear1(l):
    global search
    global searched
    global num
    search=[[weizhi[0],weizhi[1],""]]
    searched=[]
    while len(search)!=0:
        b=search.pop(0)
        if [b[0],b[1]] not in searched:
            if l[b[0]][b[1]][BOTTOM_WALL]==False :
                search.append([b[0]+1,b[1],b[2]+"U"])
                num=[b[0]+1,b[1],b[2]+"U"]
                if num[0]==0 and num[1]==size[1]-1:
                    break
            if l[b[0]][b[1]][RIGHT_WALL]==False:
                search.append([b[0],b[1]+1,b[2]+"L"])
                num=[b[0],b[1]+1,b[2]+"L"]
                if num[0]==0 and num[1]==size[1]-1:
                    break
            if l[b[0]-1][b[1]][BOTTOM_WALL]==False:
                search.append([b[0]-1,b[1],b[2]+"D"])
                num=[b[0]-1,b[1],b[2]+"D"]
                if num[0]==0 and num[1]==size[1]-1:
                    break
            if l[b[0]][b[1]-1][RIGHT_WALL]==False:
                search.append([b[0],b[1]-1,b[2]+"R"])
                num=[b[0],b[1]-1,b[2]+"R"]
                if num[0]==0 and num[1]==size[1]-1:
                    break
        searched.append([b[0],b[1]])
def sear2(l):
    global search
    global searched
    global num
    search=[[weizhi2[0],weizhi2[1],""]]
    searched=[]
    while len(search)!=0:
        b=search.pop(0)
        if [b[0],b[1]] not in searched:
            if l[b[0]][b[1]][BOTTOM_WALL]==False :
                search.append([b[0]+1,b[1],b[2]+"U"])
                num=[b[0]+1,b[1],b[2]+"U"]
                if num[0]==0 and num[1]==size[1]-1:
                    break
            if l[b[0]][b[1]][RIGHT_WALL]==False:
                search.append([b[0],b[1]+1,b[2]+"L"])
                num=[b[0],b[1]+1,b[2]+"L"]
                if num[0]==0 and num[1]==size[1]-1:
                    break
            if l[b[0]-1][b[1]][BOTTOM_WALL]==False:
                search.append([b[0]-1,b[1],b[2]+"D"])
                num=[b[0]-1,b[1],b[2]+"D"]
                if num[0]==0 and num[1]==size[1]-1:
                    break
            if l[b[0]][b[1]-1][RIGHT_WALL]==False:
                search.append([b[0],b[1]-1,b[2]+"R"])
                num=[b[0],b[1]-1,b[2]+"R"]
                if num[0]==0 and num[1]==size[1]-1:
                    break
        searched.append([b[0],b[1]])
def movetringle(event):
    if event.keysym == 'Up' and maze[weizhi[0]-1][weizhi[1]][BOTTOM_WALL]== False:
        canvas.move(yuan,0,-10) 
        weizhi[0]=weizhi[0]-1##第一个参数使画布上所画的形状的ID数字，第二个是对x（水平方向）坐标增加的值，第三个是对y（垂直方向）坐标增加的值
    elif event.keysym == 'Down' and maze[weizhi[0]][weizhi[1]][BOTTOM_WALL]== False:
        canvas.move(yuan,0,10)
        weizhi[0]=weizhi[0]+1
    elif event.keysym == 'Left' and maze[weizhi[0]][weizhi[1]-1][RIGHT_WALL]== False:
        canvas.move(yuan,-10,0)
        weizhi[1]=weizhi[1]-1
    elif event.keysym =='Right' and maze[weizhi[0]][weizhi[1]][RIGHT_WALL]== False :
        canvas.move(yuan,10,0)
        weizhi[1]=weizhi[1]+1
    else:
        canvas.move(yuan,0,0)
    if weizhi==[0,size[1]-1]:
        messagebox.showinfo(title='Tql!!!', message='你已经通关了，大神1！')
canvas.bind_all('<KeyPress-Up>',movetringle)  ##让tkinter监视KeyPress事件，当该事件发生时调用movetriangle函数
canvas.bind_all('<KeyPress-Down>',movetringle)
canvas.bind_all('<KeyPress-Left>',movetringle)
canvas.bind_all('<KeyPress-Right>',movetringle)  


flag1=0
flag2=0

def tishi():
    global l1
    global flag1
    if flag1==1:
        return
    l1=[]
    sear1(maze)
    s=num[2]
    s=s[::-1]
    r=size[1]*10
    c=10
    for i in s:
        if i=="L":
            r-=10
        elif i=="R":
            r+=10
        elif i=="U":
            c-=10
        elif i=="D":
            c+=10
        if flag1==0:
            w=drawCircle(canvas, r, c, 3, fill = "pink")
            l1.append(w)
    flag1=1

def tishi2():
    global l2
    global flag2
    if flag2==1:
        return
    l2=[]
    sear2(maze)
    s=num[2]
    s=s[::-1]
    r=size[1]*10
    c=10
    for i in s:
        if i=="L":
            r-=10
        elif i=="R":
            r+=10
        elif i=="U":
            c-=10
        elif i=="D":
            c+=10
        if flag2==0:
            v=drawCircle(canvas, r, c, 3, fill = "green")
            l2.append(v)
    flag2=1
def ti():
    global flag1
    global flag2
    for i in l1:
        canvas.delete(i)
    for j in l2:
        canvas.delete(j)
    flag1=0
    flag2=0

l = Label(king, bg='red', fg='black',font=('Arial', 12), width=5,text="起点")
l.grid(row=2,column=0,sticky=NE)

r = Label(king, bg='yellow', fg='black',font=('Arial', 12), width=5,text="终点")
r.grid(row=0,column=2,sticky=SW)

b = Button(king, text='玩家1提示', font=('Arial', 12), width=10, height=1, command=tishi)
b.grid(row=2,column=1)
b2= Button(king, text='玩家2提示', font=('Arial', 12), width=10, height=1, command=tishi2)
b2.grid(row=3,column=1)

c = Button(king, text='隐藏路线', font=('Arial', 12), width=10, height=1, command=ti)
c.grid(row=4,column=1)
def movetringle1(event):
    if event.keysym == 'W' and maze[weizhi2[0]-1][weizhi2[1]][BOTTOM_WALL]== False:
        canvas.move(yuan2,0,-10) 
        weizhi2[0]=weizhi2[0]-1##第一个参数使画布上所画的形状的ID数字，第二个是对x（水平方向）坐标增加的值，第三个是对y（垂直方向）坐标增加的值
    elif event.keysym == 'S' and maze[weizhi2[0]][weizhi2[1]][BOTTOM_WALL]== False:
        canvas.move(yuan2,0,10)
        weizhi2[0]=weizhi2[0]+1
    elif event.keysym == 'A' and maze[weizhi2[0]][weizhi2[1]-1][RIGHT_WALL]== False:
        canvas.move(yuan2,-10,0)
        weizhi2[1]=weizhi2[1]-1
    elif event.keysym =='D' and maze[weizhi2[0]][weizhi2[1]][RIGHT_WALL]== False :
        canvas.move(yuan2,10,0)
        weizhi2[1]=weizhi2[1]+1
    else:
        canvas.move(yuan2,0,0)
    if weizhi2==[0,size[1]-1]:
        messagebox.showinfo(title='Tql!!!', message='你已经通关了，大神2！')
canvas.bind_all('<KeyPress-W>',movetringle1)  ##让tkinter监视KeyPress事件，当该事件发生时调用movetriangle函数
canvas.bind_all('<KeyPress-S>',movetringle1)
canvas.bind_all('<KeyPress-A>',movetringle1)
canvas.bind_all('<KeyPress-D>',movetringle1)    
     
king.mainloop()