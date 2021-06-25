# https://www.hackerrank.com/challenges/s10-the-central-limit-theorem-3/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = float(input())
m = float(input())
s = float(input())
i = float(input())
z = float(input())

std = s/(n**0.5)
print(round(m-std*z,2))
print(round(m+std*z,2))