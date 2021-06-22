def factorial(num):
    return 1 if num == 0 else num*factorial(num-1)
answer1 = 0
answer2 = 0

x,y = list(map(int, input().split(" ")))
p = x/100
for z in range(3):
    temp1 = (factorial(y) / (factorial(z) * factorial(y-z))) * p**z * (1-p)**(y-z)
    answer1 = answer1 + temp1
print(round(answer1,3))
for z in range(2, y+1):
    temp2 = (factorial(y) / (factorial(z) * factorial(y-z))) * p**z * (1-p)**(y-z)
    answer2 = answer2 + temp2
print(round(answer2,3))