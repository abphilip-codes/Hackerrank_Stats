# https://www.hackerrank.com/challenges/s10-pearson-correlation-coefficient/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
s1 = s2 = cov = 0

x = list(map(float,input().strip().split()))
ux = sum(x)/n
for X in x:
    s1 =  s1+(X-ux)**2
stdx = (s1/n)**0.5

y = list(map(float,input().strip().split()))
uy = sum(y)/n
for Y in y:
    s2 =  s2+(Y-uy)**2
stdy = (s2/n)**0.5

for i in range(n):
    cov = cov + ((x[i]-ux)*(y[i]-uy))
print(round(cov/(n*stdx*stdy),3))