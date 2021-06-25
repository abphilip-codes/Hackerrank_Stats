# https://www.hackerrank.com/challenges/s10-the-central-limit-theorem-2/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
x = float(input())
n = int(input())
mu = float(input())
si = float(input())

m = n*mu
s = math.sqrt(n)*si
print(round(0.5*(1+math.erf((x-m)/(s*math.sqrt(2)))),4))