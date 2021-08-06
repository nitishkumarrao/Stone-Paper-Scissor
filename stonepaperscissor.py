import random
temp='y'
while temp=='y':
  print('Hi there, lets play STONE PAPER SCISSOR ',end='\n')
  print()
  print('Pick your choice: stone | paper | scissors')

  user_choice = input()
  options=['stone','paper','scissors']
  print(f'You chose: {user_choice}')
    
  computer_choice = random.choice(options)
  print(f'Computer chose chose: {computer_choice}')

  if user_choice in options:
    if computer_choice == user_choice:
      print('draw')
    elif computer_choice=='stone':
      if user_choice=='scissors':
        print('compuer won!')
      else:
        print('You won!')
    elif computer_choice=='scissors':
        if user_choice=='paper':
          print('compuer won!')
        else:
          print('You won!')
    elif computer_choice=='paper':
        if user_choice=='stone':
          print('compuer won!')
        else:
          print('You won!')
  else:
    print('You made an invalid choice! ')
  
  print('Do you want to play again? Y/N: ')
  temp=input().lower()

if temp=='n':
   print('Thank you for joining')
else:
    print('You made an invalid choice! ')