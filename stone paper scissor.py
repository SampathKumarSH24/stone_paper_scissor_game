
import random
def gameWin(comp,you): 
 if comp == you:
  return None
 elif comp == 'r':
  if you == 's':
   return False 
  else:
   return True
 elif comp == 'p':
  if you == 'r':
   return False
  else:
   return True
 elif comp == 's':
  if you == 'p':
   return False
  else:
   return True
 

randNo = random.randint(1,3)   
if randNo == 1:
 comp = 'r'
elif randNo == 2:
 comp = 'p'
elif randNo == 3:
 comp = 's'

while(1):
 print("Comp Turn: Rock(r), Paper(p) or Scissor(s)?")
 you = input("Your's Turn: Rock(r), Paper(p) or Scissor(s) or quit(q)?")
 
 a = gameWin(comp,you)

 print(f"Computer chose {comp}")
 print(f"You chose {you}")

 if a == None:
  print("The game is tie!")
 elif a:
  print("You win!")
 else:
  print("You lose!")
 print("\nNEXT  ROUND\n")

 if you == 'q':
  print("game over")
  break 
 else:
  continue

print("Thank You")
