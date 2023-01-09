from random import randint

correct_answer = randint(1,100)

user_answer = int(input("1부터 100사이의 값을 입력해주세요:")

print(f"입력하신 {user_answer}과 정답인 {correct_answer}가 {user_answer==correct_answer}")
