# https://www.hackerrank.com/challenges/s10-the-central-limit-theorem-1/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
x = int(input())
n = int(input())
mu = int(input())
si = int(input())

m = n*mu
s = math.sqrt(n)*si
Z = (x-m)/s
print(round(0.5*(1+math.erf(Z/math.sqrt(2))),4))