# https://www.hackerrank.com/challenges/s10-spearman-rank-correlation-coefficient/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
d = 0

x = list(map(float,input().strip().split()))
xr1 = dict((X, i+1) for i, X in enumerate(sorted(set(x))))
xr2 = [xr1[X] for X in x]

y = list(map(float,input().strip().split()))
yr1 = dict((Y, i+1) for i, Y in enumerate(sorted(set(y))))
yr2 = [yr1[Y] for Y in y]

for i in range(n):
    d = d + (xr2[i] -yr2[i])**2
print(round(1-(6*d)/(n*(n*n-1)),3))