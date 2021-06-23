x,y=map(int,input().split())
z=int(input())
p=x/y
q=1-p
print(round((q**(z-1))*p,3))