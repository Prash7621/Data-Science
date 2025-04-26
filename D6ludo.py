won_number=6
throw_count=0
throw_limit=2
while throw_count < throw_limit:
    throw=int(input("Throw your dir and enter your number : "))
    throw_count +=1
    if throw == won_number:
      print("You won")
      break
    else:
       print("you lose the game , try again!")
       print("Hint : if you won the game you want number 6 in die")