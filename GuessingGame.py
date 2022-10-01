import random
valid_input = [1,2,3,4,5]
print("Welcome to Guessing Game!")
print("Please choose the difficulty!")
print("1 for extremely easy\n2 for easy\n3 for medium\n4 for hard\n5 for extremely hard")
def game(difficulty):
#extremely easy
    if difficulty == '1':
        print("You have 3 guesses to find out our magic number from 0 to 10. Ready?")
        number = random.randint(0,10)
        num = 0
        for num in range(0,3):
            guess = int(input("What is your guess?"))
            if guess < number:
                print(f'Higher. You have {2-num} guesses left')
                num+=1
            elif guess > number:
                print(f'Lower. You have {2-num} guesses left') 
                num+=1   
            elif guess == number:
                print(f'You got the number - it is {number}. Congratulations!')
                break
        if num == 3:
            print(f'You lost. The magic number is {number}')
    #easy
    elif difficulty == '2':
        print("You have 5 guesses to find out our magic number from 0 to 100. Ready?")
        number = random.randint(0,100)
        num = 0
        for num in range(0,5):
            guess = int(input("What is your guess?"))
            if guess < number:
                print(f'Higher. You have {4-num} guesses left')
                num+=1
            elif guess > number:
                print(f'Lower. You have {4-num} guesses left') 
                num+=1   
            elif guess == number:
                print(f'You got the number - it is {number}. Congratulations!')
                break
        if num == 5:
            print(f'You lost. The magic number is {number}')
    #medium
    elif difficulty == '3':
        print("You have 7 guesses to find out our magic number from 0 to 1000. Ready?")
        number = random.randint(0,1000)
        num = 0
        for num in range(0,7):
            guess = int(input("What is your guess?"))
            if guess < number:
                print(f'Higher. You have {6-num} guesses left')
                num+=1
            elif guess > number:
                print(f'Lower. You have {6-num} guesses left') 
                num+=1   
            elif guess == number:
                print(f'You got the number - it is {number}. Congratulations!')
                break
        if num == 7:
            print(f'You lost. The magic number is {number}')
    #hard
    elif difficulty == '4':
        print("You have 9 guesses to find out our magic number from 0 to 10000. Ready?")
        number = random.randint(0,10000)
        num = 0
        for num in range(0,9):
            guess = int(input("What is your guess?"))
            if guess < number:
                print(f'Higher. You have {8-num} guesses left')
                num+=1
            elif guess > number:
                print(f'Lower. You have {8-num} guesses left') 
                num+=1   
            elif guess == number:
                print(f'You got the number - it is {number}. Congratulations!')
                break
        if num == 9:
            print(f'You lost. The magic number is {number}')
    #extremely hard
    elif difficulty == '5':
        print("You have 11 guesses to find out our magic number from 0 to 100000. Ready?")
        number = random.randint(0,100000)
        num = 0
        for num in range(0,11):
            guess = int(input("What is your guess?"))
            if guess < number:
                print(f'Higher. You have {10-num} guesses left')
                num+=1
            elif guess > number:
                print(f'Lower. You have {10-num} guesses left') 
                num+=1   
            elif guess == number:
                print(f'You got the number - it is {number}. Congratulations!')
                break
        if num == 11:
            print(f'You lost. The magic number is {number}')
    #error handle
    elif difficulty not in valid_input:
        print("Wrong input, please enter valid number!")
        print("Please choose the difficulty!")
        print("1 for extremely easy\n2 for easy\n3 for medium\n4 for hard\n5 for extremely hard")
        game(input())
game(input())