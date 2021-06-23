def geo_dist(n, p):
    return (1-p)**(n-1) * p

x, y = map(int, input().split())
p = x/y
answer = 0
for z in range(1,n+1):
    answer = answer + temp
n = int(input())
print(round(sum([geo_dist(i, p) for i in range(1,n+1)]),3))