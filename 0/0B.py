# https://www.hackerrank.com/challenges/s10-weighted-mean/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
length = int(input())
n = list(map(int, input().split(" ")))
w = list(map(int, input().split(" ")))
print("%.1f"%(sum(list(map(lambda x:x[0]*x[1],zip(n, w))))/sum(w)))