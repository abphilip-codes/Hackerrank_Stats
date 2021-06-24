# https://www.hackerrank.com/challenges/s10-poisson-distribution-1/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import exp
def factorial(num):
    return 1 if num == 0 else num*factorial(num-1)
x = float(input())
y = int(input())
answer = ((x ** y) * exp(-x)) / factorial(y)
print(round(answer,3))