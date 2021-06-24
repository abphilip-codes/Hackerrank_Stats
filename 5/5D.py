# https://www.hackerrank.com/challenges/s10-normal-distribution-2/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
m, sd = list(map(int, input().split(" ")))
q1 = int(input())
q2 = int(input())
print(round((1-0.5*(1 + math.erf((q1-m)/(sd*(2**0.5)))))*100,2))
print(round((1-0.5*(1 + math.erf((q2-m)/(sd*(2**0.5)))))*100,2))
print(round((0.5*(1 + math.erf((q2-m)/(sd*(2**0.5)))))*100,2))