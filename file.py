"""
Created on Tue Jun 11 21:43:01 2019

@author: 33805
"""
T=int(input())
l=[]
shuchu=[]
for i in range(T):
    flag=1
    num=[]
    n=int(input())
    e=list(map(int,input().split()))
    f=list(map(int,input().split()))
    for j in range(n-1):
        nu=e[j+1]-e[j]
        num.append(nu)
    for j in range(n-1):
        nm=f[j+1]-f[j]
        if nm in num:
            flag=1
        else:
            flag=0
    if flag==1:
        shuchu.append("YES")
    else:
        shuchu.append("NO")
for i in shuchu:
    print(i)
for i in shuchu:
    print(i)
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
