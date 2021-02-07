# https://www.hackerrank.com/challenges/s10-quartiles/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
from statistics import median
n=int(input())
a=[int(x) for x in input().split()]
a.sort()

l=int(len(a)/2)
if len(a)%2!=0:
    lower=a[:l]
    upper=a[l+1:]
else:
    lower=a[:l]
    upper=a[l:]

print(int(median(lower)))
print(int(median(a)))
print(int(median(upper)))