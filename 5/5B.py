# https://www.hackerrank.com/challenges/s10-poisson-distribution-2/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
x,y = list(map(float, input().split(" ")))
cost1 = 160 + 40*(x+x**2)
cost2 = 128 + 40*(y+y**2)
print(round(cost1, 3))
print(round(cost2, 3))