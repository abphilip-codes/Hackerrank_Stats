# https://www.hackerrank.com/challenges/s10-interquartile-range/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
import statistics as stats
n = int(input())
v = list(map(int, input().split()))
f = list(map(int, input().split()))

arr = []
for i in range(n):
    arr += [v[i]] * f[i]
N = sum(f)
arr.sort()

if n%2==0:
    Q1 = stats.median(arr[:N//2])
    Q3 = stats.median(arr[N//2:]) 
else:
    Q1 = stats.median(arr[:N//2])
    Q3 = stats.median(arr[N//2+1:])
range1 = round(float(Q3-Q1), 1)
print(range1)