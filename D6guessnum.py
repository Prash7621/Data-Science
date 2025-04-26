secret_number=8
guess_count=0
guess_limit=5
while guess_count < guess_limit :
    guess_number = int(input("Guess a number between 1 and 20: "))
    guess_count +=1
    
    if guess_number ==secret_number :
        print("Congratulation , you guess the correct number")
        break
    elif guess_number < secret_number :
        print("Too low")
    elif guess_number > secret_number:
        print("Too high")
    
print("Game Over")