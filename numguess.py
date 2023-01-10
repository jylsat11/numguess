from random import randint
from time import sleep

correct_answer = randint(1,100)

user_answer = int(input("please enter one number between 1 and 100"))

print(f" it is {user_answer==correct_answer} that your answer {user_answer} and {correct_answer} is the same number")

if user_answer == correct_answer:
    print('**************************************')
    sleep(1)
    print(f"Congrat!!!!! the answer is {correct_answer}.")
elif user_answer > correct_answer:
    print(f"Wrong answer !! the answer is smaller than your answer {user_answer}")
elif user_answer < correct_answer:
    print(f"Wrong answer !! the answer is larger than your answer {user_answer}")
