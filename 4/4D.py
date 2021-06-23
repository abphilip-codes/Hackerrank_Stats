# https://www.hackerrank.com/challenges/s10-geometric-distribution-2/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
x,y = map(int, input().split())
p = x/y
n = int(input())
answer = 0

for z in range(1,n+1):
    temp = (1-p)**(z-1) * p
    answer = answer + temp
print(round(answer,3))