# https://www.hackerrank.com/challenges/s10-multiple-linear-regression/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
import math
x = []
y = []
z = []

m,n = [int(Z) for Z in input().strip().split(' ')]
for Z in range(n):
    d = input().strip().split(' ')
    x.append(d[:m])
    y.append(d[m:])
    
o = int(input().strip())
for Z in range(o):
    z.append(input().strip().split(' '))

x = np.array(x,float)
y = np.array(y,float)
z = np.array(z,float)

xr = x-np.mean(x,axis=0)
yr = y-np.mean(y)
zr = z-np.mean(x,axis=0)
b = np.dot(np.linalg.inv(np.dot(xr.T,xr)),np.dot(xr.T,yr))

wr = np.dot(zr,b)
w = wr+np.mean(y)

for i in w:
    print(round(float(i),2))