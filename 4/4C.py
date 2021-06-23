# https://www.hackerrank.com/challenges/s10-geometric-distribution-1/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
x,y=map(int,input().split())
z=int(input())
p=x/y
q=1-p
print(round((q**(z-1))*p,3))