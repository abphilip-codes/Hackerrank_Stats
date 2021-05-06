# https://www.hackerrank.com/challenges/s10-standard-deviation/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input().strip())
all1 = [int(i) for i in input().strip().split()]

u = sum(all1) / n
v = sum(((i - u) ** 2) for i in all1)/n
sd = v ** 0.5
print("{0:0.1f}".format(sd))    