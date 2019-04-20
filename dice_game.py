import random

dice = [1, 2, 3, 4, 5, 6]
answer = input("You tryin' to play some dice?: ").strip().lower()
pcount = 0
ccount = 0
while answer != '':
  if answer[0] == 'y':
    print ("Cool! Type 'stop' to end, iight?\n")
    print ("I'll roll first!")
    print ('...rolling...\n')
    comp = random.choice(dice)
    print ("I just rolled a * {} *".format(comp))
    if comp > 4:
      print ("oouuu, try to beat that!")
    elif comp > 2:
      print ('meh, I still got this thou')
    else:
      print ('Damn!')
    input ("\nPress 'Enter' to roll...\n")
    player1 = random.choice(dice)
    print ("You've rolled a * {} *\n".format(player1))
    if comp > player1:
      print ('lol')
      ccount += 1
    elif comp < player1:
      print ('You got lucky son!')
      pcount += 1
    else:
      print ('Tied up.')
    answer = input('\ntryna go again?').strip().lower()
  elif answer[0] == 'n':
    print ("Say no more son, be on your way then slime.")
    break
  else:
    print ("It was a simple 'Yes' or 'No' question!")
    break

if answer == '':
  print ("You did not answer with 'yay' or 'nay'.")
else:
  print ('Final Score is {} to {}.'.format(ccount,pcount))
  if pcount > ccount:
    print ("Quitting while you're ahead, I see.")
  elif pcount < ccount:
    print ('Get smoked!')
  else:
    print ("Na, run that back.")
