# https://www.hackerrank.com/challenges/s10-geometric-distribution-1/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import erf
m, sd = list(map(int, input().split(" ")))
q1 = float(input())
q2a, q2b = list(map(float, input().split(" ")))
p1 = 0.5 + 0.5 *erf((q1-m)/(sd*2**0.5))
p2 = 0.5*erf((q2b-m)/(sd*2**0.5)) - 0.5*erf((q2a-m)/(sd*2**0.5))
print(round(p1,3))
print(round(p2,3))