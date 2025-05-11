import random
n = random.randint(1,100)
a = -1
guesses = 0
while(a!=n):
    a = int(input("Enter a number: "))
    guesses += 1
    if(a>n):
        print(f"Guess the number which is lesser than {a}")
    elif(a<n):
         print(f"Guess the number have value is greater than {a}")
    elif(a==n):
        print("Congratulations your guess is correct!!")
        print(f"You took {guesses} attempts")
    else:
        print("Something is wrong")





