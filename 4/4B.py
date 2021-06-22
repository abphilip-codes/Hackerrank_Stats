def factorial(num):
    return 1 if num == 0 else num*factorial(num-1)

x,y = list(map(float, input().split(" ")))
odds = x/y
answer = 0
for z in range(3,7):
    temp1 = factorial(6)/(factorial(z)*factorial(6-z))
    temp2 = temp1*((odds/(1+odds))**z)*((1-(odds/(1+odds)))**(6-z))
    answer = answer+temp2
print(round(answer,3))