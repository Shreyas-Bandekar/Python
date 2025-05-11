import random
n = random.randint(1,100)
a = -1

while(a!=n):
    a = int(input("Enter a number: "))
    if(a>n):
        print(f"Guess the number which is lesser than {a}")
    elif(a<n):
         print(f"Guess the number have value is greater than {a}")
    elif(a==n):
        print("Congratulations your guess is correct!!")
    else:
        print("Something is wrong")


