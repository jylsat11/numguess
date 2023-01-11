from random import randint
from time import sleep


def user_input()->int:
  user_answer = int(input("please enter one integer number (1~100): "))
  return user_answer

def numguess(user_answer:int, correct_answer:int):
  if user_answer == correct_answer:
      return 'same'

  elif user_answer > correct_answer:
      return 'larger'
  else:
      return 'smaller'


correct_answer = randint(1,100)


for i in range(10+1):
  user_answer = user_input()
  result = numguess(user_answer,correct_answer)
  if result == 'same':
    print(f"Congrat. your answer {user_answer} and correct answer {correct_answer} is the same number.")
    break
  elif result == 'larger':
    print(f"wrong. your asnwer {user_answer} is larger than the correct answer.")
    print("please enter the number again (1~100).")
  else:
    print(f"wrong. Your answer {user_answer} is smaller than the correct answer.")
    print("please enter the number again (1~100).")    

print("The game is over.")
