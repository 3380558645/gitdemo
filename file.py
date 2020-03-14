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