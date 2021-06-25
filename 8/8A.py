# https://www.hackerrank.com/challenges/s10-least-square-regression-line/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
user = [map(int, input().split()) for z in range(5)]
ax, ay, ax2, axy = map(sum, zip(*[(x, y, x**2, x * y) for x, y in user]))
m = (5*axy-ax*ay)/(5*ax2-ax**2)
c = (ay/5)-m*(ax/5)
# y = mx+c, x=80
print(round(m*80+c,3))