import random
def guessnumber():
    print("Hello! What is your name?")
    name=input()
    print("Well, " + name +  ", I am thinking of a number between 1 and 20.")
    print("Take a guess")
    r=random.randint(1, 20)
    cnt=0
    while True:
        n=int(input())
        if n<r:
            print("Your guess is too low.")
            print("Take a guess")
            cnt+=1
        elif n>r:
            print("Your guess is too high.")
            print("Take a guess")
            cnt+=1
        elif n==r:
            cnt+=1
            break
    print("Good job, " + name + "! You guessed my number in " + str(cnt) + " guesses!")

guessnumber()