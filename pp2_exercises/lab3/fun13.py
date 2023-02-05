def guess_the_number(n):
    print("Hello! What is your name?")
    name=input()
    print("Well, "+name+", I am thinking of a number between 1 and 20.")
    print("Take a guess.")
    number1=int(input())
    times=1
    while number1:
        if(number1==n):
            print("Good job, KBTU! You guessed my number in "+str(times)+" guesses!")
            number1=int(input())
        elif(number1<n):
            print("Your guess is too low.")
            print("Take a guess.")
            times=times+1
            number1=int(input())
        elif(number1>n):
            print("Your guess is too high.")
            print("Take a guess.")
            times=times+1
            number1=int(input())