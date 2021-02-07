# https://www.hackerrank.com/challenges/s10-basic-statistics/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
from scipy import stats
import numpy 

length = int(input()) 
input1 = list(map(int, input().split()))
print(numpy.mean(input1))
print(numpy.median(input1))
print(int(stats.mode(input1)[0]))