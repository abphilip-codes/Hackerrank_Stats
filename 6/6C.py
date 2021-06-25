# https://www.hackerrank.com/challenges/s10-the-central-limit-theorem-3/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
samples = float(input())
mean = float(input())
sd = float(input())
interval = float(input())
z = float (input())

sd_sample = sd / (samples**0.5)
print(round(mean - sd_sample*z,2))
print(round(mean + sd_sample*z,2))